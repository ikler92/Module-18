from django.shortcuts import render
from .forms import UserRegister

# Псевдо-список существующих пользователей
users = ['admin', 'user1', 'testuser']


# Представление с формой Django
def sign_up_by_django(request):
    info = {'form': UserRegister()}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if username in users:
                info['error'] = 'Пользователь уже существует'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif age > 120:
                info['error'] = 'Возраст не может быть больше 120'
            else:
                info['success'] = f'Приветствуем, {username}!'
                users.append(username)
        info['form'] = form
    return render(request, 'fifth_task/registration_page.html', info)


# Представление с обычным HTML
def sign_up_by_html(request):
    info = {'form': UserRegister()}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        try:
            age = int(age)
            if age < 3 or age > 120:
                raise ValueError('Возраст вне допустимого диапазона.')
        except ValueError:
            info['error'] = 'Возраст должен быть числом от 3 до 120'
            return render(request, 'fifth_task/registration_page.html', info)

        if username in users:
            info['error'] = 'Пользователь уже существует'
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
        else:
            info['success'] = f'Приветствуем, {username}!'
            users.append(username)

    return render(request, 'fifth_task/registration_page.html', info)
