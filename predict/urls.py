from django.urls import path

from . import views

urlpatterns = [
    # ex: /register
    path('register', views.register, name='register'),
    # ex: /register/
    path('register/', views.register, name='register'),
    # ex: /about
    path('about', views.about, name='about'),
    # ex: /about/
    path('about/', views.about, name='about'),
    # ex: /leaderboard
    path('leaderboard', views.leaderboard, name='leaderboard'),
    # ex: /leaderboard/
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    #predict/{{ game.match_id }}/1/0/0"
    path('<str:gameID>/<int:guessOneWin>/<int:guessRight>/<int:guessWrong>', views.later_guess, name='guess2+'),
    # ex: /
    path('', views.first_guess, name='guess1'),
]
