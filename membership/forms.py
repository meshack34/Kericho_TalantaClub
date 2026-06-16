from django import forms
from .models import MembershipApplication


class MembershipApplicationForm(forms.ModelForm):

    class Meta:
        model = MembershipApplication

        fields = "__all__"

        widgets = {
            "date_of_birth": forms.DateInput(
                attrs={"type": "date"}
            ),
            "medical_information": forms.Textarea(
                attrs={"rows": 4}
            ),
        }