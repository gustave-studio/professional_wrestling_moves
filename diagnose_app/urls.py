from django.urls import path, include
from .views import testfunc

urlpatterns = [
    path('test/', testfunc, name='test'),
]
