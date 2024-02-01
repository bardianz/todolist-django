from django.contrib import admin
from todo_app.models import ToDoItem

# Register your models here.


class ToDoItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'checked', 'description', 'owner',)


admin.site.register(ToDoItem, ToDoItemAdmin)
