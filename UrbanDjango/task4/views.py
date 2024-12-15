from django.shortcuts import render


# Главная страница
def main_view(request):
    return render(request, 'fourth_task/main.html', {'pagename': 'Главная страница'})


# Магазин
def games_view(request):
    games = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    return render(request, 'fourth_task/games.html', {'pagename': 'Игры', 'games': games})


# Корзина
def cart_view(request):
    return render(request, 'fourth_task/cart.html', {'pagename': 'Корзина'})
