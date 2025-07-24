from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import CustomUser
from accounts.utils import send_approval_notification_email


# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = [
        "first_name",
        "last_name",
        "email",
        "position",
        "is_verified",
        "is_approved",
        "is_active",
        "date_joined",
        "last_login",
        "approval_actions",
    ]
    list_filter = [
        "is_verified",
        "is_approved", 
        "is_active",
        "position",
        "date_joined",
    ]
    search_fields = ["email", "first_name", "last_name"]
    ordering = ["-date_joined"]
    
    actions = ["approve_users", "reject_users", "mark_verified"]
    
    def approval_actions(self, obj):
        """Display approve/reject buttons for each user"""
        if obj.is_verified and not obj.is_approved:
            # User is verified but not approved - show approve button
            approve_url = reverse('admin:approve_user', args=[obj.id])
            return format_html(
                '<a class="button" href="{}" style="background: #28a745; color: white; padding: 5px 10px; text-decoration: none; border-radius: 3px;">Approve</a>',
                approve_url
            )
        elif obj.is_verified and obj.is_approved:
            # User is verified and approved - show reject button
            reject_url = reverse('admin:reject_user', args=[obj.id])
            return format_html(
                '<a class="button" href="{}" style="background: #dc3545; color: white; padding: 5px 10px; text-decoration: none; border-radius: 3px;">Reject</a>',
                reject_url
            )
        else:
            # User is not verified - show status
            return format_html(
                '<span style="color: #6c757d;">Not Verified</span>'
            )
    approval_actions.short_description = "Actions"
    
    def get_urls(self):
        from django.urls import path
        urls = super().get_urls()
        custom_urls = [
            path(
                '<uuid:user_id>/approve/',
                self.admin_site.admin_view(self.approve_user_view),
                name='approve_user',
            ),
            path(
                '<uuid:user_id>/reject/',
                self.admin_site.admin_view(self.reject_user_view),
                name='reject_user',
            ),
        ]
        return custom_urls + urls
    
    def approve_user_view(self, request, user_id):
        """Handle individual user approval"""
        try:
            user = CustomUser.objects.get(id=user_id)
            if user.is_verified and not user.is_approved:
                user.is_approved = True
                user.is_active = True
                user.save()
                send_approval_notification_email(user, approved=True)
                messages.success(request, f"User {user.get_full_name()} has been approved.")
            else:
                messages.error(request, "User cannot be approved (not verified or already approved).")
        except CustomUser.DoesNotExist:
            messages.error(request, "User not found.")
        
        return HttpResponseRedirect(reverse('admin:users_customuser_changelist'))
    
    def reject_user_view(self, request, user_id):
        """Handle individual user rejection"""
        try:
            user = CustomUser.objects.get(id=user_id)
            if user.is_approved:
                user.is_approved = False
                user.is_active = False
                user.save()
                send_approval_notification_email(user, approved=False)
                messages.success(request, f"User {user.get_full_name()} has been rejected.")
            else:
                messages.error(request, "User is not approved.")
        except CustomUser.DoesNotExist:
            messages.error(request, "User not found.")
        
        return HttpResponseRedirect(reverse('admin:users_customuser_changelist'))
    
    def approve_users(self, request, queryset):
        for user in queryset:
            if not user.is_approved and user.is_verified:
                user.is_approved = True
                user.is_active = True
                user.save()
                # Send approval notification
                send_approval_notification_email(user, approved=True)
        
        self.message_user(request, f"{queryset.count()} user(s) have been approved.")
    approve_users.short_description = "Approve selected users"
    
    def reject_users(self, request, queryset):
        for user in queryset:
            if user.is_approved:
                user.is_approved = False
                user.is_active = False
                user.save()
                # Send rejection notification
                send_approval_notification_email(user, approved=False)
        
        self.message_user(request, f"{queryset.count()} user(s) have been rejected.")
    reject_users.short_description = "Reject selected users"
    
    def mark_verified(self, request, queryset):
        updated = queryset.update(is_verified=True)
        self.message_user(request, f"{updated} user(s) have been marked as verified.")
    mark_verified.short_description = "Mark selected users as verified"


admin.site.register(CustomUser, CustomUserAdmin)
