from django.contrib import admin
from .models import Todo
# Register your models here.

admin.site.register(Todo)    #registering todo model in the admin
class Todo(admin.ModelAdmin):
    list_display = ('title', 'details', 'user')