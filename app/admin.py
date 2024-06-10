from django.contrib import admin
from .models import Add, Author


# Register your models here.
@admin.register(Add)
class AddAdmin(admin.ModelAdmin):
    list_display = ['header', 'add_id', 'author', 'position', 'views']
    ordering = ['-views']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']
