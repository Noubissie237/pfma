from django.contrib import admin
from .models import *
# Register your models here.

class AdminGenre(admin.ModelAdmin):
    list_display = ('genre',)

class AdminUsers(admin.ModelAdmin):
    list_display = ('nom', 'email', 'genre', 'pwd')


admin.site.register(Users, AdminUsers),
admin.site.register(Genre, AdminGenre),