from django.contrib import admin
from .models import ToDolist,Item
# Register your models here.
admin.site.register(ToDolist)
admin.site.register(Item)