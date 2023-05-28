from django.db import models


class Client(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]

    CONTACT_CHOICES = [
        ('email', 'Email'),
        ('phone', 'Phone'),
        ('none', 'None')
    ]

    name = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profile_images/')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    nationality = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    education_background = models.TextField()
    preferred_mode_of_contact = models.CharField(
        max_length=10, choices=CONTACT_CHOICES)

    def __str__(self):
        return self.name
