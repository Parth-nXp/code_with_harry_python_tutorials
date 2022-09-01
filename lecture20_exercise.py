"""
Guess the number game. Consider a random number and take input from user and check if the input of user is equal to random number or not. If number is greater than random number tell the user to enter smaller number, if smaller then tell to enter the greater number.
Note: User will have a limited number of guesses that is 9. You have to also print number of guesses left for user. Also if the user wins print how many guesses he took to win the game.
"""

number = 18
num_of_guess = 9

while num_of_guess > 0:
    number = input("Enter your guess!!  ")
    num_of_guess -= 1
    if int(number) < 18:
        print("Guessed value is less. Enter a greater number")
        print("Number of attempts left: " + str(num_of_guess))
    elif int(number) > 18:
        print("Guessed value is more. Enter a lesser number")
        print("Number of attempts left: " + str(num_of_guess))
    else:
        print("You have enterd a correct number. Congratulations!!!!!!!")
        print("You took "+str(9-num_of_guess)+" guesses.")
        break
if num_of_guess == 0:
    print("Game Over")
