from django.urls import path
from . import views

urlpatterns = [
    path('function/', views.function_view, name='func_view'),
    path('class/', views.class_view, name='class_view'),

]