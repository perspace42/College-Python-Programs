'''
Author: Scott Field
Version: 1.0
Date: 1/31/2022
Program Name: Sum_Of_All_Single_Digit_Numbers
Purpose: Calculate the sum of all single digit numbers entered in an input string that contains no spaces
'''

#Welcome Message
print("Please enter a string containing only single digit numbers without spaces, this program will output the sum of the entered numbers.\n")

#Initialize Variables
numbers = "0123456789"
user_input = ""
program_output = 1
loop = True

#User Input & Validation Loop
while (loop):
    #Assume the Input is valid until proven otherwise
    loop = False

    #Get User Input
    user_input = input("Please enter a string of single digit numbers (0-9) without spaces to be added together.\n:")

    #Check that the input contains only numbers
    for index in range(0,len(user_input)):
        if (user_input[index] not in numbers):
            print(f"Error: '{user_input[index]}' is not a valid single digit number.")
            print("(This loop will continue until a valid single digit number/numbers (0-9) is/are entered.)\n")

            #If the input is not a number (invalid input) prompt the user for a number (valid input)
            loop = True
            
            #if an incorrect input has been found, restart the loop without checking for more
            break
        
       
        
    
#Convert the String of Characters to Integers Then Add them Together
length = len(user_input)
sum_of_numbers = 0

program_output = 0

for index in range(0,length):
    sum_of_numbers += int(user_input[index])

#Output the sum of the entered numbers
program_output = sum_of_numbers
print(f"The sum of the single digit numbers: '{user_input}' = {program_output}")


    





    
            
