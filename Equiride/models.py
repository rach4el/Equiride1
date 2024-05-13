from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    STATUS = ((0, "Draft"), (1, "Published"))

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="review_posts"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)

class Event(models.Model):
    event_name = models.CharField(max_length=200, unique=True)
    location = models.CharField(max_length=200)
    date = models.DateTimeField()

    def __str__(self):
        return self.event_name

class Booking(models.Model):
    booking_holder = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="users_booking"
    )
    date_issued = models.DateTimeField(auto_now_add=True)
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="event_booking"
    )

    def __str__(self):
        return f"Booking_for {self.booking_holder}"