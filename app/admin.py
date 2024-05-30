from django.contrib import admin
from .models import *

class MovieActorInline(admin.TabularInline):
    model = MovieActor
    extra = 1

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'duration', 'rating')
    search_fields = ('title', 'rating')
    list_filter = ('release_date', 'rating')
    inlines = [MovieActorInline]

class UserCollectionAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'date_added')
    search_fields = ('user__username', 'movie__title')
    list_filter = ('date_added',)

admin.site.register(Genre)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Movie, MovieAdmin)
admin.site.register(User)
admin.site.register(UserCollection, UserCollectionAdmin)
