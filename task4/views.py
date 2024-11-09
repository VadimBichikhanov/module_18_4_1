from django.shortcuts import render

def index(request):
    context = {
        'games': ['Atomic Heart', 'Cyberpunk 2077']
    }
    return render(request, 'fourth_task/index.html', context)

def about(request):
    return render(request, 'fourth_task/about.html')

def contact(request):
    return render(request, 'fourth_task/contact.html')

def shop(request):
    games = ['Atomic Heart', 'Cyberpunk 2077']
    return render(request, 'fourth_task/shop.html', {'games': games})