from django.shortcuts import render
from .models import List

def home(request):

    all_items = List.objects.all

    return render(request, 'home.html', {'todo_items': all_items})

def about(request):
    my_name = "Anthony Bonello"
    number = 2 + 2
    context = {'name': my_name, 'number': number}
    return render(request, 'about.html', context)