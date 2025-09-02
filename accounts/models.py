from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    GENDER_CHOICES = (("M", "Male"), ("F", "Female"))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=150, blank=True)
    dob = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    mobile = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.full_name if self.full_name else self.user.username
    
    class Meta:
        db_table = "profile"