from django.contrib import admin
from .models import Categories, Studio, Platform, Game

admin.site.register(Categories)
admin.site.register(Studio)
admin.site.register(Platform)
admin.site.register(Game)
# Register your models here.
