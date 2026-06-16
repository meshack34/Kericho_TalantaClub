from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import MembershipApplicationForm


def membership(request):

    if request.method == "POST":

        form = MembershipApplicationForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Membership application submitted successfully."
            )

            return redirect("membership")

    else:
        form = MembershipApplicationForm()

    context = {
        "form": form
    }

    return render(
        request,
        "membership/membership.html",
        context
    )
