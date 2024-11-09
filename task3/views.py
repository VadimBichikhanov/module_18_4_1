from django.shortcuts import render

def index(request):
    return render(request, 'third_task/index.html')

def shop(request):
    items = [
        {'name': 'Игра 1'},
        {'name': 'Игра 2'},
        {'name': 'Игра 3'},
    ]
    return render(request, 'third_task/shop.html', {'items': items})

def cart(request):
    return render(request, 'third_task/cart.html')