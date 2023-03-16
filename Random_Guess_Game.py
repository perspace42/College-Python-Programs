'''
Author: Scott Field
Version: 1.0
Program Name: Random_Guess_Game
Program Purpose: Store a random number between rangelow and rangehigh, the user then attempts to guess that number with messages of To Low, and To High offering clues.
'''
#Import Libraries
import random

#Initialize Variables
guess = 101
num_guesses = 0
range_low = 1
range_high = 100

#Whether the loop should continue
loop = True

#Whether the input is valid
valid = False

random_num = random.randint(range_low,range_high)

#User Input & Input Validation
while (loop):
    user_input = input(f"Please guess a random number whose value is between between {range_low} and {range_high} . \n:")

    #attempt to convert input to integer
    try:

        guess = int(user_input)
        valid = True
    except:
        #Ensure only integer guesses are counted
        print(f"Error, the guess must be an integer, this loop will continue until a valid integer is entered.")
        loop = True
        valid = False


    #Game Loop
    if (valid):
        #Increment the number of valid guesses entered
        num_guesses += 1
        if guess == random_num:
            print(f"Congratulations you guessed the number {random_num} in {num_guesses} attempts.")
            loop = False
    
        elif guess < random_num:
            print("Too low, try again.")
    
        else:
            print("Too High, try again")






    

