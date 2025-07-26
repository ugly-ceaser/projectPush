from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import Category, Tag, BlogPost, BlogImage, Comment, BlogSettings


class BlogImageInline(admin.TabularInline):
    model = BlogImage
    extra = 1
    fields = ("image", "caption", "alt_text", "order")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "post_count", "created_at")
    list_filter = ("created_at",)
    search_fields = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}

    def post_count(self, obj):
        return obj.posts.count()

    post_count.short_description = "Posts"


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "post_count")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}

    def post_count(self, obj):
        return obj.posts.count()

    post_count.short_description = "Posts"


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "category",
        "status",
        "is_featured",
        "view_count",
        "created_at",
    )
    list_filter = ("status", "is_featured", "category", "tags", "created_at", "author")
    search_fields = ("title", "excerpt", "content")
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("tags",)
    inlines = [BlogImageInline]
    date_hierarchy = "created_at"
    actions = ["make_published", "make_draft", "make_featured"]

    fieldsets = (
        (
            "Basic Information",
            {"fields": ("title", "slug", "author", "category", "tags")},
        ),
        ("Content", {"fields": ("excerpt", "content", "featured_image")}),
        (
            "SEO",
            {"fields": ("meta_title", "meta_description"), "classes": ("collapse",)},
        ),
        (
            "Publication",
            {
                "fields": ("status", "is_featured", "published_at"),
                "classes": ("collapse",),
            },
        ),
    )

    readonly_fields = ("view_count", "created_at", "updated_at")

    def save_model(self, request, obj, form, change):
        if not change:  # If creating a new post
            obj.author = request.user
        super().save_model(request, obj, form, change)

    def make_published(self, request, queryset):
        queryset.update(status="published")

    make_published.short_description = "Mark selected posts as published"

    def make_draft(self, request, queryset):
        queryset.update(status="draft")

    make_draft.short_description = "Mark selected posts as draft"

    def make_featured(self, request, queryset):
        queryset.update(is_featured=True)

    make_featured.short_description = "Mark selected posts as featured"


@admin.register(BlogImage)
class BlogImageAdmin(admin.ModelAdmin):
    list_display = ("post", "image_preview", "caption", "order")
    list_filter = ("post",)
    search_fields = ("caption", "post__title")

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit: cover;" />',
                obj.image.url,
            )
        return "No Image"

    image_preview.short_description = "Preview"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("author_name", "post", "status", "created_at", "is_reply")
    list_filter = ("status", "created_at", "post")
    search_fields = ("content", "guest_name", "guest_email", "author__email")
    actions = ["approve_comments", "reject_comments"]

    def author_name(self, obj):
        return obj.author_name

    author_name.short_description = "Author"

    def is_reply(self, obj):
        return bool(obj.parent)

    is_reply.boolean = True
    is_reply.short_description = "Reply"

    def approve_comments(self, request, queryset):
        queryset.update(status="approved")

    approve_comments.short_description = "Approve selected comments"

    def reject_comments(self, request, queryset):
        queryset.update(status="rejected")

    reject_comments.short_description = "Reject selected comments"


@admin.register(BlogSettings)
class BlogSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not BlogSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


# Custom admin site configuration
admin.site.site_header = "Blog Administration"
admin.site.site_title = "Blog Admin Portal"
admin.site.index_title = "Welcome to Blog Administration"
