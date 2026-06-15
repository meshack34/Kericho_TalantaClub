from django.db import models

class Membership(models.Model):

    full_name = models.CharField(
        max_length=200
    )

    phone = models.CharField(
        max_length=20
    )

    email = models.EmailField()

    dob = models.DateField()

    category = models.CharField(
        max_length=100
    )

    created = models.DateTimeField(
        auto_now_add=True
    )