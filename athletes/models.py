from django.db import models

class Athlete(models.Model):

    name = models.CharField(max_length=200)

    photo = models.ImageField(
        upload_to='athletes/'
    )

    category = models.CharField(
        max_length=100
    )

    achievements = models.TextField()

    def __str__(self):
        return self.name