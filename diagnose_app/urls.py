from django.urls import path, include
from .views import topfunc, resultfunc
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('top/', topfunc, name='top'),
    path('result/', resultfunc, name='result')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
