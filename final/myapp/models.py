from django.db import models
from django.contrib.auth.hashers import make_password
from django.core.validators import RegexValidator


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class CustomUser(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email


class Client(models.Model):
    y_name = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=100)
    profile = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=15, help_text='Enter your phone number (e.g., +1234567890)')
    linkedin = models.CharField(max_length=200, blank=True, null=True, help_text='Enter your LinkedIn profile URL')
    experience = models.TextField(blank=True, null=True)
    education = models.TextField()
    languages = models.TextField()
    skills = models.TextField(blank=True, null=True)
    certificate = models.TextField(blank=True, null=True)
    extracurricular_activities = models.CharField(max_length=200, blank=True, null=True, validators=[RegexValidator(regex='^[^;]*$', message='Invalid input. Please avoid using semicolons.')])

    def __str__(self):
        return self.y_name
