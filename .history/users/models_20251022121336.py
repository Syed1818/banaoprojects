# users/models.py

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    # Define choices for the user type
    USER_TYPE_CHOICES = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
    )
    
    # Link to the built-in User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Additional fields from the task
    profile_picture = models.ImageField(upload_to='profile_pics/')
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return f'{self.user.username} Profile'
