from django.shortcuts import render

def login(request):
    context = {
        'title': 'HappyToes - LogIn',
    }
    return render(request, 'users/login.html', context)


def logout(request):
    context = {
        'title': 'HappyToes - LogOut',
    }
    return render(request, 'users/logout.html', context)


def registration(request):
    context = {
        'title': 'HappyToes - Регистрация',
    }
    return render(request, 'users/registration.html', context)


def profile(request):
    context = {
        'title': 'HappyToes - Мой профиль',
    }
    return render(request, 'users/profile.html', context)