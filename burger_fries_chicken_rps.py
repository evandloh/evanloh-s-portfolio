# Bonus project rock paper scissors
# 7/09/2020
#
#############################################

import random

choices = ['fries','burger','chicken']
#Rock = fries, paper = burger, scissors = chicken
Username = input('Please enter your player name: ')

print('Welcome',Username, 'to the game of Burger, Fries, and Chicken!')
print('Chicken beats burger, burger beats fries, fries beats chicken')

for i in range(3):
    player_choice = input('Please enter either Fries, burger, or chicken: ')
    computer_choice = random.choice(choices)

    print('You chose',player_choice,'and the computer chose',computer_choice)

    if player_choice == computer_choice:
        print('Aww you tied, better luck next time')

    elif player_choice == 'fries':
        if computer_choice == 'chicken':
            print('You win! GG')
        else:
            print('You Lost!!, Try again')
    elif player_choice == 'chicken':
        if computer_choice == 'burger':
            print('You win! GG')
        else:
            print('You lost!!, Try again')
    elif player_choice == 'burger':
        if computer_choice == 'fries':
            print('You win! GG')
        else:
            print('You lost!, try again')

    else:
        print('Thats not a choice, Try again')
