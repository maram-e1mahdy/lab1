from django.shortcuts import render
import random

def rock_paper_scissors(request):
    
    player_choice = request.GET.get('choice')

    
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)

    
    result = None
    player_image = None
    computer_image = None

    
    if player_choice:
        player_image = f'images/{player_choice}.png'
        computer_image = f'images/{computer_choice}.png'

        if player_choice == computer_choice:
            result = "It's a Tie!"
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'scissors' and computer_choice == 'paper') or \
             (player_choice == 'paper' and computer_choice == 'rock'):
            result = "You Win!"
        else:
            result = "You Lose!"

    #
    return render(request, 'play/game.html', {
        'result': result,
        'player_image': player_image,
        'computer_image': computer_image,
    })


