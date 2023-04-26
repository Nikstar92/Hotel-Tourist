from django.contrib import admin

from .models import *


class ApartamentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name')
    list_display_links = ('id', 'email', 'first_name')
    search_fields = ('email', 'first_name')


admin.site.register(Apartaments, ApartamentsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(User, UserAdmin)
