from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Movie, MovieActor
from .forms import MovieForm

# Create a new movie
def home_view(request):
    return render(request, 'home.html')


def create_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'movies/movie_form.html', {'form': form})

# Read and list all movies
def movie_list(request):
    movies = Movie.objects.all().order_by('title')
    return render(request, 'movies/movie_list.html', {'movies': movies})

# Read and detail view for a single movie
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    movie_actors = MovieActor.objects.filter(movie=movie).order_by('actor__last_name', 'actor__first_name')
    return render(request, 'movies/movie_detail.html', {'movie': movie, 'movie_actors': movie_actors})

# Update an existing movie
def update_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movies/movie_form.html', {'form': form})

# Delete an existing movie
def delete_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movie_list')
    return render(request, 'movies/movie_confirm_delete.html', {'movie': movie})


def movie_list_by_letter(request, letter):
    movies = Movie.objects.filter(title__istartswith=letter).order_by('title')
    return render(request, 'movies/movie_list_by_letter.html', {'movies': movies, 'letter': letter})


@login_required
def profile(request):
    return render(request, 'registration/profile.html')