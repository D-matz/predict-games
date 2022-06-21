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
    top_ten = MyUser.objects.order_by('-guesses_right')[:10]
    for u in top_ten:
        numgames = u.guesses_right + u.guesses_wrong
        if numgames > 0:
            u.correctRate = u.guesses_right/(numgames)
        else:
            u.correctRate = 0
    context = {
        "userlist": top_ten
    }
    return render(request, 'predict/leaderboard.html', context)

def about(request):
    return render(request, 'predict/about.html')

def get_unseen_game():
    g = Game.objects.filter(seen_before=False).filter(seen_by_one=False).first()
    g.seen_by_one = True
    g.save()
    return g.id
def first_guess(request):
    #logged in user - show their current game
    if request.user.is_authenticated:
        user = MyUser.objects.get(username=request.user.username)
        user_guess_game = user.currently_guessing
        if user_guess_game == "none":
            user_guess_game = get_unseen_game()
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
        randomgame = Game.objects.filter(seen_before=True).order_by('?').first()
        context = {
            'new_game': randomgame,
        }
        return render(request, 'predict/firstguess.html', context)

def later_guess(request, gameID, guessOneWin, guessRight, guessWrong):
    #show hidden game if it's currently guessing one or what
    #logged in user - if current game record result and update current game, show their current game
    if request.user.is_authenticated:
        user = MyUser.objects.get(username=request.user.username)
        user_guess_game = user.currently_guessing
        lastResult = Game.objects.get(id=gameID)
        context = {}
        if user_guess_game == "none":
            user_guess_game = get_unseen_game()
            user.currently_guessing = user_guess_game
            user.save()
        elif user.currently_guessing == gameID:
            oldg = Game.objects.get(id=user.currently_guessing)
            oldg.seen_before = True
            oldg.save()
            guessOne = False
            if guessOneWin: guessOne = True
            if lastResult.teamOneWin == guessOne:
                user.guesses_right = user.guesses_right + 1
            else:
                user.guesses_wrong = user.guesses_wrong + 1
            user_guess_game = get_unseen_game()
            user.currently_guessing = user_guess_game
            user.save()
        newGame = Game.objects.get(id=user.currently_guessing)
        context['new_game'] = newGame
        context['guessRight'] = user.guesses_right
        context['guessWrong'] = user.guesses_wrong
        context['last_game'] = lastResult
        user.save()
        return render(request, 'predict/laterguess.html', context)

    #not logged in user - add to tally based on result of game
    else:
        randomgame = Game.objects.filter(seen_before=True).order_by('?').first()
        lastResult = Game.objects.filter(seen_before=True).get(id=gameID)
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
#fix logout also make sure setting seen before and stuff properly also maybe make a function to get new unseen game

#they see - previous result, game to guess
#url has - previous game id, previous guess, num correct, num incorrect

#you can leave but if you log in again get same game
#don't add until game guessed
#add only for game they guess
#really just one page but whatever

#logged in player
    #previous game - show result of now guessed currently_guessing
    #current game - when they guess currently guessing, give a new currently_guessing - choose game not seen_before and not seen_by_one
#logged out player - show whichever game they ask for, if game seen before
    #previous game - show only from seen games, prev game based on url
    #current game - take from seen games, current game random
