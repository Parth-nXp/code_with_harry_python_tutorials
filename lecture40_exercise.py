'''
Snake, Water, Gun game design:
Use random function with random.choice module to select 
use while loop to play this game 10 times
choose a random choice from snake water and gun and save it in variable
take input from the user what he/she has choosen from the list
tell the user after each chance who wins 
at the end of 10 rounds tell who is the winner
'''

import random
chance = 0
game_choice = ['snake', 'water', 'gun']
user_win = 0
computer_win = 0


while chance < 10:
    computer_choice = random.choice(game_choice)
    user_choice = input("Enter 1 for SNAKE, 2 for WATER, and 3 for GUN: ")

    if user_choice == '1':
        if computer_choice == 'snake':
            print('Computer choose SNAKE')
            print('Its a tie')
        elif computer_choice == 'water':
            print('Computer choose WATER')
            print('User Wins')
            user_win += 1
        else:
            print('Computer choose GUN')
            print('Computer Wins')
            computer_win += 1

    elif user_choice == '2':
        if computer_choice == 'snake':
            print('Computer choose SNAKE')
            print('Computer Wins')
            computer_win += 1
        elif computer_choice == 'water':
            print('Computer choose WATER')
            print('Its a tie')
        else:
            print('Computer choose GUN')
            print('User Wins')
            user_win += 1

    elif user_choice == '3':
        if computer_choice == 'snake':
            print('Computer choose SNAKE')
            print('User Wins')
            user_win += 1
        elif computer_choice == 'water':
            print('Computer choose WATER')
            print('Computer Wins')
            computer_win += 1
        else:
            print('Computer choose GUN')
            print('Its a tie')

    else:
        print('Wrong Input!')
    chance += 1

if user_win < computer_win:
    print('So the winner is USER')
elif user_win > computer_win:
    print('So the winner is COMPUTER')
else:
    print('This is a tie')
