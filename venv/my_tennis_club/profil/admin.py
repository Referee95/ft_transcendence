from django.contrib import admin
from .models import UserAccount, Tournament, Game

# Register your models here.



admin.site.register(UserAccount)
admin.site.register(Tournament)
admin.site.register(Game)