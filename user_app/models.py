from django.db import models
from django.contrib.auth.models import User


class UserPosition(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название должности")

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.ForeignKey(UserPosition, verbose_name="Должность", related_name="user_profile", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Create your models here.
