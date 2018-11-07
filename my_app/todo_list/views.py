from django.shortcuts import render
from .models import List
from .forms import ListForm
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
        else:
            pass
        all_items = List.objects.all
        messages.success(request, ('Item has been successfully added to the list.'))
        return render(request, 'home.html', {'todo_items': all_items})
    else: 
        all_items = List.objects.all
        return render(request, 'home.html', {'todo_items': all_items})

def about(request):
    my_name = "Anthony Bonello"
    number = 2 + 2
    context = {'name': my_name, 'number': number}
    return render(request, 'about.html', context)