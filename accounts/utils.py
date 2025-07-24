from django.utils import timezone
from umuahia_ireland.settings import DEFAULT_EMAIL, Admin_Email
from django.core.mail import send_mail


def send_verification_email(user, subject, message, html_message=None):
    send_mail(
        subject,
        message,
        DEFAULT_EMAIL,
        [user.email],
        html_message=html_message,
        fail_silently=False,
    )


def send_admin_notification_email(user):
    """Send notification to admin about new user registration"""
    subject = f"New User Registration: {user.get_full_name()}"
    message = f"""
    A new user has registered and requires approval:
    
    Name: {user.get_full_name()}
    Email: {user.email}
    Position: {user.position}
    Date Registered: {user.date_joined}
    
    Please review and approve/reject this user in the admin panel.
    """
    
    send_mail(
        subject,
        message,
        DEFAULT_EMAIL,
        [Admin_Email],
        fail_silently=False,
    )


def send_approval_notification_email(user, approved=True):
    """Send notification to user about approval status"""
    if approved:
        subject = f"Account Approved - Welcome to Umuahia Community Ireland!"
        message = f"""
        Dear {user.get_full_name()},
        
        Your account has been approved by the administrator. You can now log in and access your account.
        
        Best regards,
        Umuahia Community Ireland Team
        """
    else:
        subject = f"Account Status Update - Umuahia Community Ireland"
        message = f"""
        Dear {user.get_full_name()},
        
        Your account registration has been reviewed. Unfortunately, your account has not been approved at this time.
        
        If you believe this is an error, please contact support.
        
        Best regards,
        Umuahia Community Ireland Team
        """
    
    send_mail(
        subject,
        message,
        DEFAULT_EMAIL,
        [user.email],
        fail_silently=False,
    )
