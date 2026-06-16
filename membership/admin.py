from django.contrib import admin
from django.contrib import admin
from .models import MembershipApplication


@admin.register(MembershipApplication)
class MembershipApplicationAdmin(admin.ModelAdmin):

    list_display = (
        "first_name",
        "last_name",
        "membership_type",
        "phone_number",
        "email",
        "created_at",
    )

    search_fields = (
        "first_name",
        "last_name",
        "email",
        "phone_number",
    )

    list_filter = (
        "membership_type",
        "gender",
        "created_at",
    )
