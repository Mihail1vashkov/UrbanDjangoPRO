from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart_view, name='cart_view'),
    path('games/', views.games_view, name='games_view'),
    path('platform/', views.platform_view, name='platform_view'),
    path('menu/', views.menu_view, name='menu_view')

]