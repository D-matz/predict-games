from django.contrib import admin
from .models import Game, MyUser
from django.contrib.auth.admin import UserAdmin

class UserAdmin(UserAdmin):
    list_display = (
        'username', 'guesses_right', 'guesses_wrong', 'currently_guessing'
        )

admin.site.register(Game)

admin.site.register(MyUser, UserAdmin)
