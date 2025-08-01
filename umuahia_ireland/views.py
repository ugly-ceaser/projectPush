from umuahia_ireland.settings import Admin_Email
from django.core.mail import send_mail

from .utils import send_verification_email
from django.contrib.auth.models import User
from django.http import JsonResponse  # Add this import
from django.shortcuts import render  # Add this import for rendering templates


EMAIL_DIR = "../templates/registration/email"


def send_email(request):
    if request.method == "POST":
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Compose the email message
        subject = f"New Contact Form Submission from {name} {surname}"
        body = f"""
        Name: {name}
        Surname: {surname}
        Email: {email}
        Message: {message}
        """
        admin_email = Admin_Email

        try:
            send_mail(
                subject,
                body,
                email,
                [admin_email],
                html_message=None,
                fail_silently=False,
            )

            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})

    return JsonResponse({"success": False, "error": "Invalid request method"})


def privacy_statement(request):
    return render(request, 'privacy_statement.html')
