from django.shortcuts import render, redirect
from .models import Movie, MovieList
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User, auth


@login_required(login_url='login')
def index(request):
    movies = Movie.objects.all()
    featured_movie = movies[len(movies) - 1]
    most_views = Movie.objects.order_by('-movie_views')
    context = {
        'movies': movies,
        'featured_movie': featured_movie,
        'most_views': most_views
    }

    return render(request, 'index.html', context)


@login_required(login_url='login')
def movie(request, pk):
    movie_id = pk
    movie_details = Movie.objects.get(movie_id=movie_id)
    movie_details.movie_views += 1
    movie_details.save()
    context = {
        'movie_details': movie_details
    }
    return render(request, 'movie.html', context)


@login_required(login_url='login')
def genre(request, pk):
    movie_genre = pk
    movies = Movie.objects.filter(genre=movie_genre)
    context = {
        'movies': movies,
        'movie_genre': movie_genre,
    }
    return render(request, 'genre.html', context)


@login_required(login_url='login')
def search(request):
    if request.method == 'POST':
        search_term = request.POST['search_term']
        movies = Movie.objects.filter(title__icontains=search_term)
        context = {
            'search_term': search_term,
            'movies': movies,
        }
        return render(request, 'search.html', context)

    else:
        return redirect('/')


@login_required(login_url='login')
def my_list(request):
    movie_list = MovieList.objects.filter(owner_user=request.user)
    user_movie_list = []
    for movie in movie_list:
        user_movie_list.append(movie.movie)

    context = {
        'movies': user_movie_list
    }
    return render(request, 'my_list.html', context)


@login_required(login_url='login')
def add_to_list(request, movie_id):
    if request.method == 'POST':
        user = request.user
        movie = get_object_or_404(Movie, movie_id=movie_id)

        if MovieList.objects.filter(owner_user=user, movie=movie).exists():
            messages.info(request, 'Movie already in list')
            return redirect('movie', pk=movie_id)

        movie_list_entry = MovieList.objects.create(owner_user=user, movie=movie)
        movie_list_entry.save()
        messages.info(request, 'Added ✓')
        return redirect('movie', pk=movie_id)


    else:
        return redirect('/')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid!')
            return redirect('login')

    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken !')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken!')
                return redirect('signup')

            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                # now login user
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)
                return redirect('/')
        else:
            messages.info(request, 'Password Not Matching !')
            return redirect('signup')

    else:
        return render(request, 'signup.html')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')
