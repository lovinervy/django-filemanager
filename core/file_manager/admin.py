from django.contrib import admin
from .models import Directory, File


@admin.register(Directory)
class DirectoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    search_fields = ('name',)

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('name', 'directory', 'file')
    search_fields = ('name',)
