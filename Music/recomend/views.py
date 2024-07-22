from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from recomend.forms import LoginForm, RegisterForm
from recomend.models import Music
import random


def doLogout(request):
    logout(request)
    return redirect('login')


def home(request):
    ids = Music.objects.all()
    info = Music.objects.get(id=random.randint(1, len(ids)))
    day_author = info.artist
    day_music = info.name
    id_day = info.id
    is_authenticated = False
    if request.user.is_authenticated:
        is_authenticated = True
    return render(request, 'index.html', {'id': id_day, 'music' : day_music, 'author': day_author, 'is_authenticated': is_authenticated})


def loginPage(request):
    if not request.user.is_authenticated:
        form = LoginForm()
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
                if user is not None:
                    login(request, user)
                    return redirect('login')
                else:
                    form.add_error(None, 'Неверные данные!')
        return render(request, 'login.html', {'form': form})
    else:
        return redirect('home')


def registerPage(request):

    # инициализируем объект формы
    form = RegisterForm()

    if request.method == 'POST':
        # заполняем объект данными формы, если она была отправлена
        form = RegisterForm(request.POST)

        if form.is_valid():
            # если форма валидна - создаем нового пользователя
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            return redirect('login')
    # ренедерим шаблон и передаем объект формы
    return render(request, 'registration.html', {'form': form})


def profile(request):
    is_authenticated = False
    if request.user.is_authenticated:
        is_authenticated = True
    first_name = request.user.username
    return render(request, 'profile.html', {'name': first_name, 'is_authenticated': is_authenticated})


def song(request, id: int):
    is_authenticated = False
    if request.user.is_authenticated:
        is_authenticated = True
    info = Music.objects.get(id=id)
    genres = Music.objects.filter(genre__icontains=info.genre)
    artist = Music.objects.filter(artist=info.artist)
    return render(request, 'music.html', {'author': artist,'music': genres, 'genre': info.genre, "path_to_song": info.path_to_song,
                                          "path_to_img": info.path_to_img, "name": info.name, "artist": info.artist, 'is_authenticated': is_authenticated})


def search_suggestions(request):
    query = request.GET.get('query', '')
    results = Music.objects.filter(name__icontains=query) | Music.objects.filter(artist__icontains=query)
    suggestions = [{'id': result.id, 'title': result.name, 'artist': result.artist} for result in results]
    return JsonResponse(suggestions, safe=False)


