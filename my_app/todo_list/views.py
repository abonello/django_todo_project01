from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def about(request):
    my_name = "Anthony Bonello"
    number = 2 + 2
    context = {'name': my_name, 'number': number}
    return render(request, 'about.html', context)