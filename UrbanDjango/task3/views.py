from django.shortcuts import render


# Главная страница
def main_view(request):
    return render(request, 'third_task/main.html')


# Магазин
def games_view(request):
    games = {
        "Atomic Heart": "Купить",
        "Cyberpunk 2077": "Купить",
        "PayDay 2": "Купить"
    }
    return render(request, 'third_task/games.html', {'games': games})


# Корзина
def cart_view(request):
    return render(request, 'third_task/cart.html')
