from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Director(models.Model):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Actor(models.Model):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Movie(models.Model):
    RATING = {
        "G": "G",
        "PG": "PG",
        "PG-13": "PG-13",
        "R": "R",
        "NC-17": "NC-17",
    }
    title = models.CharField(max_length=200, blank=True)
    release_date = models.IntegerField(null=True, blank=True)
    duration = models.PositiveIntegerField(null=True, blank=True, help_text="Duration in minutes")
    rating = models.CharField(max_length=10, blank=True, choices=RATING)
    plot_summary = models.TextField(blank=True)
    poster_url = models.URLField(blank=True)
    genres = models.ManyToManyField(Genre, related_name='movies', blank=True)
    directors = models.ManyToManyField(Director, related_name='movies', blank=True)
    actors = models.ManyToManyField(Actor, through='MovieActor', blank=True)

    def __str__(self):
        return self.title
    
    def actor_names(self):
        return ', '.join([])

class MovieActor(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.actor} as {self.role} in {self.movie}'

class User(models.Model):
    username = models.CharField(max_length=100, unique=True, blank=True)
    email = models.EmailField(unique=True, blank=True)
    password = models.CharField(max_length=100, blank=True)
    join_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username

class UserCollection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='collections')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='collections')
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} collection: {self.movie.title}'
