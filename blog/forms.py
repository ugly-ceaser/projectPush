from django import forms
from django.forms import inlineformset_factory
from .models import BlogPost, BlogImage, Comment, Category, Tag


class BlogPostForm(forms.ModelForm):
    """Form for creating and editing blog posts"""

    class Meta:
        model = BlogPost
        fields = [
            "title",
            "category",
            "tags",
            "excerpt",
            "content",
            "featured_image",
            "meta_title",
            "meta_description",
            "status",
            "is_featured",
        ]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
                    "placeholder": "Enter blog post title",
                }
            ),
            "excerpt": forms.Textarea(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
                    "rows": 3,
                    "placeholder": "Brief description of the post",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 editor",
                    "id": "editor",
                    "rows": 15,
                }
            ),
            "category": forms.Select(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                }
            ),
            "tags": forms.CheckboxSelectMultiple(attrs={"class": "space-y-2"}),
            "featured_image": forms.FileInput(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 file:mr-4 file:py-2 file:px-4 file:rounded-md file:border-0 file:text-sm file:font-medium file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100",
                    "accept": "image/*",
                }
            ),
            "meta_title": forms.TextInput(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
                    "placeholder": "SEO title (optional)",
                }
            ),
            "meta_description": forms.Textarea(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
                    "rows": 2,
                    "placeholder": "SEO description (optional)",
                }
            ),
            "status": forms.Select(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                }
            ),
            "is_featured": forms.CheckboxInput(
                attrs={
                    "class": "h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
                }
            ),
        }


class BlogImageForm(forms.ModelForm):
    """Form for blog images"""

    class Meta:
        model = BlogImage
        fields = ["image", "caption", "alt_text", "order"]
        widgets = {
            "image": forms.FileInput(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 file:mr-4 file:py-2 file:px-4 file:rounded-md file:border-0 file:text-sm file:font-medium file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100",
                    "accept": "image/*",
                }
            ),
            "caption": forms.TextInput(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
                    "placeholder": "Image caption (optional)",
                }
            ),
            "alt_text": forms.TextInput(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
                    "placeholder": "Alt text for accessibility",
                }
            ),
            "order": forms.NumberInput(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
                    "min": 0,
                }
            ),
        }


# Create formset for multiple images
BlogImageFormSet = inlineformset_factory(
    BlogPost, BlogImage, form=BlogImageForm, extra=3, can_delete=True
)


class CommentForm(forms.ModelForm):
    """Form for user comments"""

    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
                    "rows": 4,
                    "placeholder": "Write your comment here...",
                }
            )
        }


class GuestCommentForm(forms.ModelForm):
    """Form for guest comments"""

    class Meta:
        model = Comment
        fields = ["guest_name", "guest_email", "content"]
        widgets = {
            "guest_name": forms.TextInput(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
                    "placeholder": "Your name",
                }
            ),
            "guest_email": forms.EmailInput(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
                    "placeholder": "Your email (optional)",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
                    "rows": 4,
                    "placeholder": "Write your comment here...",
                }
            ),
        }


class CategoryForm(forms.ModelForm):
    """Form for creating categories"""

    class Meta:
        model = Category
        fields = ["name", "description"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
                    "placeholder": "Category name",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
                    "rows": 3,
                    "placeholder": "Category description (optional)",
                }
            ),
        }


class TagForm(forms.ModelForm):
    """Form for creating tags"""

    class Meta:
        model = Tag
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
                    "placeholder": "Tag name",
                }
            )
        }


class BlogSearchForm(forms.Form):
    """Form for searching blog posts"""

    query = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "class": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
                "placeholder": "Search posts...",
            }
        ),
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        empty_label="All Categories",
        widget=forms.Select(
            attrs={
                "class": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
            }
        ),
    )
    tag = forms.ModelChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        empty_label="All Tags",
        widget=forms.Select(
            attrs={
                "class": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
            }
        ),
    )
