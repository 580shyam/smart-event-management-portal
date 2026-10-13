from django.conf import settings
from django.db import models
from django.utils.text import slugify


class Event(models.Model):
    CATEGORY_CHOICES = [
        ("technology", "Technology"),
        ("education", "Education"),
        ("business", "Business"),
        ("culture", "Culture"),
        ("sports", "Sports"),
        ("other", "Other"),
    ]

    title = models.CharField(max_length=180)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="other")
    description = models.TextField()
    venue = models.CharField(max_length=200)
    event_date = models.DateTimeField()
    capacity = models.PositiveIntegerField(default=50)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_events",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["event_date"]

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title) or "event"
            slug = base_slug
            counter = 2
            while Event.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    @property
    def registration_count(self):
        return self.registrations.count()

    @property
    def available_seats(self):
        return max(self.capacity - self.registration_count, 0)

    @property
    def is_full(self):
        return self.available_seats <= 0

    def __str__(self):
        return self.title


class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="registrations")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="event_registrations",
    )
    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-registered_at"]
        constraints = [
            models.UniqueConstraint(fields=["event", "user"], name="unique_user_event_registration")
        ]

    def __str__(self):
        return f"{self.user.username} — {self.event.title}"
