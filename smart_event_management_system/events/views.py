from django.contrib import messages
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.db import IntegrityError, transaction
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST

from .forms import SignUpForm
from .models import Event, Registration


def home(request):
    events = Event.objects.filter(event_date__gte=timezone.now()).order_by("event_date")
    query = request.GET.get("q", "").strip()
    category = request.GET.get("category", "").strip()
    if query:
        events = events.filter(Q(title__icontains=query) | Q(venue__icontains=query) | Q(description__icontains=query))
    valid_categories = {value for value, _label in Event.CATEGORY_CHOICES}
    if category in valid_categories:
        events = events.filter(category=category)
    return render(request, "events/home.html", {
        "events": events,
        "query": query,
        "selected_category": category,
        "categories": Event.CATEGORY_CHOICES,
    })


def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    is_registered = request.user.is_authenticated and event.registrations.filter(user=request.user).exists()
    return render(request, "events/event_detail.html", {"event": event, "is_registered": is_registered, "now": timezone.now()})


def signup_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    form = SignUpForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, "Your account is ready. Welcome to Evently!")
        return redirect("dashboard")
    return render(request, "registration/signup.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        messages.success(request, f"Welcome back, {user.username}!")
        next_url = request.POST.get("next") or request.GET.get("next")
        if next_url and next_url.startswith("/") and not next_url.startswith("//"):
            return redirect(next_url)
        return redirect("dashboard")
    return render(request, "registration/login.html", {"form": form, "next": request.GET.get("next", "")})


@require_POST
@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("home")


@require_POST
@login_required
def register_for_event(request, slug):
    try:
        with transaction.atomic():
            event = Event.objects.select_for_update().get(slug=slug)
            if event.event_date < timezone.now():
                messages.error(request, "Registration is closed because this event has already started.")
                return redirect("event_detail", slug=slug)
            if Registration.objects.filter(event=event, user=request.user).exists():
                messages.info(request, "You are already registered for this event.")
                return redirect("event_detail", slug=slug)
            if event.registrations.count() >= event.capacity:
                messages.error(request, "Sorry, this event is full. Please choose another event.")
                return redirect("event_detail", slug=slug)
            Registration.objects.create(event=event, user=request.user)
    except Event.DoesNotExist:
        messages.error(request, "That event could not be found.")
        return redirect("home")
    except IntegrityError:
        messages.info(request, "You are already registered for this event.")
        return redirect("event_detail", slug=slug)

    messages.success(request, f"Your seat is confirmed for {event.title}!")
    return redirect("dashboard")


@login_required
def dashboard(request):
    registrations = Registration.objects.filter(user=request.user).select_related("event")
    return render(request, "events/dashboard.html", {"registrations": registrations})


@require_POST
@login_required
def cancel_registration(request, registration_id):
    registration = get_object_or_404(Registration, pk=registration_id, user=request.user)
    event_title = registration.event.title
    registration.delete()
    messages.success(request, f"Your registration for {event_title} has been cancelled.")
    return redirect("dashboard")


def staff_check(user):
    return user.is_authenticated and user.is_staff


@user_passes_test(staff_check, login_url="login")
def admin_dashboard(request):
    context = {
        "total_events": Event.objects.count(),
        "total_users": get_user_model().objects.count(),
        "total_registrations": Registration.objects.count(),
        "upcoming_events": Event.objects.filter(event_date__gte=timezone.now()).order_by("event_date")[:6],
        "recent_registrations": Registration.objects.select_related("event", "user").order_by("-registered_at")[:8],
    }
    return render(request, "events/admin_dashboard.html", context)
