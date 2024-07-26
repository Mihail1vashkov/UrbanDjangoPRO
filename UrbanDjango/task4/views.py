from django.shortcuts import render
from django.views import View


#Классовое представление
def cart_view(request):

    return render(request, 'fourth_task/cart.html')

#Функциональное представление
def games_view(request):
    return render(request, 'fourth_task/games.html')

def platform_view(request):
    return render(request, 'fourth_task/platform.html')

def menu_view(request):
    return render(request, 'fourth_task/menu.html')
