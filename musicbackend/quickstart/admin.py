from django.contrib import admin

from .models import Setlist, Show, Patron, Song, SongSetlist
# Register your models here.
admin.site.register(Song)
admin.site.register(Setlist)
admin.site.register(Show)
admin.site.register(Patron)
admin.site.register(SongSetlist)