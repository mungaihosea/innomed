from django.urls import path
from .views import homepage, contact

urlpatterns = [
    path('', homepage, name='homepage'),
    path('contact/', contact, name='contact')
]