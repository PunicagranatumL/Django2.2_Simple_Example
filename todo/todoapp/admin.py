from django.contrib import admin
from .models import TodoItem

# Register your models here.

class TodoItemAdmin(admin.ModelAdmin):
    list_display = ("todo_item",'todo_date')

admin.site.register(TodoItem,TodoItemAdmin)