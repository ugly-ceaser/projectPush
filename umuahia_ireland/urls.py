from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404, handler500
from .errors import custom_error_404, custom_error_500
from .views import send_email, privacy_statement


handler404 = custom_error_404
handler500 = custom_error_500

urlpatterns = [
    path("", include("app.urls", namespace="app")),
    path("send-email/", send_email, name="send_email"),
    path("privacy/", privacy_statement, name="privacy_statement"),
    path("admin/", include("_admin.urls", namespace="admin")),
    path("dashboard/", include("dashboard.urls", namespace="user:")),
    path("auth/", include("accounts.urls", namespace="accounts")),
    path("auth/", include("django.contrib.auth.urls")),
    path("blog/", include("blog.urls", namespace="blog")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
