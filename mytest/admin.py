from django.contrib import admin

from .models import Musician, Album


class AlbumAdmin(admin.TabularInline):
    model = Album
    extra = 1


class MusicianAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['instrument', 'type','gender']}),
        ('name_info', {'fields': ['first_name', 'last_name'], 'classes': ['show']}),

    ]
    inlines = [AlbumAdmin]
    list_display = ('first_name', 'last_name', 'instrument', 'type')


admin.site.register(Musician, MusicianAdmin)
