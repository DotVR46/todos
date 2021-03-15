from django.contrib import admin
from .models import Category, ToDo


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed', 'created', 'updated')
    search_fields = ('title', 'description')
    odrering = ('completed', 'created')