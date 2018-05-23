from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email_address = models.EmailField(max_length=200)
    street_address = models.CharField(max_length=200)

    def __str__(self):
        return self.last_name
