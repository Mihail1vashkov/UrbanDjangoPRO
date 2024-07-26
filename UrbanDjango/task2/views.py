from django.shortcuts import render
from django.views import View


#Классовое представление
def class_view(request):
    return render(request, 'second_task/class_template.html')

#Функциональное представление
def function_view(request):
    return render(request, 'second_task/func_template.html')


# Create your views here.
