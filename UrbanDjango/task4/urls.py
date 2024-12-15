from django.urls import path
from .views import main_view, games_view, cart_view

urlpatterns = [
    path('', main_view, name='main'),
    path('games/', games_view, name='games'),
    path('cart/', cart_view, name='cart'),
]
