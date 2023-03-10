from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('ckeditor/', include("ckeditor_uploader.urls")),
    path('', include('fabrics_main.urls')),
    path('user_account/', include('user_account.urls')),
    path('about/', include('fabrics_about.urls'))

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


def get_filename(filename, request):
    return filename.upper()