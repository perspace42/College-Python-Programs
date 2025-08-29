'''
Author: Scott Field
Version: 1.0
Date: 1/31/2022
Program Name: Write_Random_To_File
Purpose: Calculate the sum of all single digit numbers entered in an input string that contains no spaces
'''

#Import Libraries
import random

#Welcome Message
print("This program will write a series of random numbers specified by the user and within range (1 - 500) to a file.\n")

#Initialization
output_file = ""
user_input = ""
output_string = ""
loop = True

random_number = 0
low_range = 1
high_range = 500
number_amount = 0

#User Input & Input Validation
while (loop):
    user_input = input("Please specify the number (integer) of random numbers to write to the file.\n:")
    try: 
        number_amount = int(user_input)

    #If the input is not an int output an error and restart the loop
    except:
        print(f"Error: '{user_input}' is not a valid integer, this loop will continue until a valid integer is entered.")

    #Otherwise the input is valid, exit the loop
    else:
        loop = False

#Create then write to the file
output_file = open("numbers.txt", "w")

#Output Header
print("\nThe random numbers added to: 'numbers.txt' are:")

for index in range(number_amount):
    #Get Random Number in Range
    random_number = random.randrange(low_range,high_range)

    #Convert Random Number to a String
    output_string = str(random_number)
    
    #Write the String to a File, Insure each subsequent number is placed on a new line (easier reading)
    output_file.write(output_string + "\n")

    #Output Random Numbers to Terminal
    print(output_string)




