from django.urls import path
from .views import sign_up_by_django, sign_up_by_html

urlpatterns = [
    path('', sign_up_by_django, name='django_sign_up'),
    path('html/', sign_up_by_html, name='html_sign_up'),
]
