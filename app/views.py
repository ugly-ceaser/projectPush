from django.shortcuts import render
from umuahia_ireland.config import APP_NAME

# Import blog models
try:
    from blog.models import BlogPost
except ImportError:
    BlogPost = None


# Create your views here.
def home(request):
    context = {}

    # Get latest blog posts if blog app is available
    if BlogPost:
        try:
            latest_posts = (
                BlogPost.objects.filter(status="published")
                .select_related("author", "category")
                .prefetch_related("tags")
                .order_by("-published_at")[:4]
            )
            context["latest_posts"] = latest_posts
        except Exception:
            # If there's any error (like table doesn't exist), just continue without blog posts
            context["latest_posts"] = []
    else:
        context["latest_posts"] = []

    return render(request, "index.html", context)
