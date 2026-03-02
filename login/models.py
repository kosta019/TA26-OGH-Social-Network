from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    password = models.CharField(max_length=24)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=1000, blank=True)
    location = models.CharField(max_length=255, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    website = models.URLField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"