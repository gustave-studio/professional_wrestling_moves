from django.urls import path, include
from .views import topfunc
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('top/', topfunc, name='top'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
