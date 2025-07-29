from django.contrib import admin
from .models import Minuites, FinancialCheckbook, Testimonial

# Register your models here.
@admin.register(Minuites)
class MinuitesAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'created_at')
    list_filter = ('date', 'created_at')
    search_fields = ('title',)
    date_hierarchy = 'created_at'


@admin.register(FinancialCheckbook)
class FinancialCheckbookAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'created_at')
    list_filter = ('date', 'created_at')
    search_fields = ('title',)
    date_hierarchy = 'created_at'


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'is_active', 'order', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'title', 'content')
    list_editable = ('is_active', 'order')
    ordering = ('order', '-created_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'title', 'content')
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Display Settings', {
            'fields': ('is_active', 'order')
        }),
    )
