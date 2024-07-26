from django.shortcuts import render
from django.views import View


#Классовое представление
def cart_view(request):
    return render(request, 'third_task/cart.html')

#Функциональное представление
def games_view(request):
    return render(request, 'third_task/games.html')

def platform_view(request):
    return render(request, 'third_task/platform.html')





# Create your views here.
