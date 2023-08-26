from django.contrib import admin
from webapp.models import Picture, Album, Favorite
class PictureAdmin(admin.ModelAdmin):
    list_display = ['id', 'caption', 'created_at']
    list_display_links = ['caption']
    search_fields = ['caption', 'author']
    readonly_fields = ['created_at']


class AlbumAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    list_display_links = ['title']
    search_fields = ['title', 'author']
    readonly_fields = ['created_at']


admin.site.register(Picture, PictureAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Favorite)
