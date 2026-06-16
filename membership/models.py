from django.db import models


class MembershipApplication(models.Model):

    MEMBERSHIP_TYPES = (
        ("Junior", "Junior Membership"),
        ("Senior", "Senior Membership"),
        ("Social", "Social Membership"),
        ("Supporter", "Supporter Membership"),
    )

    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES
    )

    date_of_birth = models.DateField()

    county = models.CharField(max_length=100)

    membership_type = models.CharField(
        max_length=20,
        choices=MEMBERSHIP_TYPES
    )

    athletic_discipline = models.CharField(
        max_length=150,
        blank=True
    )

    emergency_contact_name = models.CharField(max_length=150)

    emergency_contact_phone = models.CharField(max_length=20)

    medical_information = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"