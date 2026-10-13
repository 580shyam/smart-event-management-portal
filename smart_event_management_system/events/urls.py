from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("events/<slug:slug>/", views.event_detail, name="event_detail"),
    path("events/<slug:slug>/register/", views.register_for_event, name="register_for_event"),
    path("sign-up/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("registrations/<int:registration_id>/cancel/", views.cancel_registration, name="cancel_registration"),
    path("control-center/", views.admin_dashboard, name="admin_dashboard"),
]
