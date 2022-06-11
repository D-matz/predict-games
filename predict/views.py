from django.shortcuts import render, redirect

from .models import Game, MyUser

from django.contrib.auth import authenticate, login
from django.contrib import messages


from .forms import SignUpForm

def register(request):
    if request.method == 'POST':
        f = SignUpForm(request.POST)
        if f.is_valid():
            f.save()
            new_user = authenticate(username=f.cleaned_data['username'],
                        password=f.cleaned_data['password1'],)
            login(request, new_user)
            return redirect('/predict')

    else:
        f = SignUpForm()

    return render(request, 'predict/register.html', {'form': f})

def leaderboard(request):
    return render(request, 'predict/about.html')

def about(request):
    return render(request, 'predict/about.html')

def first_guess(request):
    #logged in user - show their current game
    if request.user.is_authenticated:
        user = MyUser.objects.get(username=request.user.username)
        user_guess_game = user.currently_guessing
        if user_guess_game == "none":
            user_guess_game = Game.objects.order_by('?').first().id
            user.currently_guessing = user_guess_game
            user.save()
        current_user_game = Game.objects.get(id=user.currently_guessing)
        context = {
            'new_game': current_user_game,
            'guessWrong': user.guesses_wrong,
            'guessRight': user.guesses_right
        }
        return render(request, 'predict/firstguess.html', context)
    #not logged in user - show any game
    else:
        randomgame = Game.objects.order_by('?').first()
        context = {
            'new_game': randomgame,
        }
        return render(request, 'predict/firstguess.html', context)

def later_guess(request, gameID, guessOneWin, guessRight, guessWrong):
    #logged in user - if current game record result and update current game, show their current game
    if request.user.is_authenticated:
        user = MyUser.objects.get(username=request.user.username)
        user_guess_game = user.currently_guessing
        lastResult = Game.objects.get(id=gameID)
        context = {}
        if user_guess_game == "none":
            user_guess_game = Game.objects.order_by('?').first().id
            user.currently_guessing = user_guess_game
        if user.currently_guessing == gameID:
            guessOne = False
            if guessOneWin: guessOne = True
            if lastResult.teamOneWin == guessOne:
                user.guesses_right = user.guesses_right + 1
            else:
                user.guesses_wrong = user.guesses_wrong + 1
            user_guess_game = Game.objects.order_by('?').first().id
            user.currently_guessing = user_guess_game
        newGame = Game.objects.get(id=user.currently_guessing)
        context['new_game'] = newGame
        context['guessRight'] = user.guesses_right
        context['guessWrong'] = user.guesses_wrong
        context['last_game'] = lastResult
        user.save()
        return render(request, 'predict/laterguess.html', context)

    #not logged in user - add to tally based on result of game
    else:
        randomgame = Game.objects.order_by('?').first()
        lastResult = Game.objects.get(id=gameID)
        guessOne = False
        if guessOneWin: guessOne = True
        context = {
        'new_game': randomgame,
        'last_game': lastResult,
        }
        if lastResult.teamOneWin == guessOne:
            context['guessRight'] = guessRight + 1
            context['guessWrong'] = guessWrong
        else:
            context['guessRight'] = guessRight
            context['guessWrong'] = guessWrong + 1
        print(guessRight,guessWrong,"context",context)
        return render(request, 'predict/laterguess.html', context)


#they see - previous result, game to guess
#url has - previous game id, previous guess, num correct, num incorrect

#you can leave but if you log in again get same game
#don't add until game guessed
#add only for game they guess
#really just one page but whatever
