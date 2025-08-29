'''
Author: Scott Field
Version: 1.0
Date: 1/24/2022
Program Name: Factorial
Purpose: Calculate the factorial of an inputed non negative integer
'''
#Welcome Message
print("This program will return the factorial of a non-negative integer inputed by the user.\n")

#Initalize Variables
user_input = ""
factorial = -1
program_output = 1
loop = True

#Input Validation
while (loop):
    user_input = input("Please enter a non negative integer to be factorialized.\n:")

    #attempt to convert input to integer
    try:

        factorial = int(user_input)
        loop = False

    except:

        #if input is not a number continue the loop
        print("Error", "'", user_input , "'" , "is not a valid non-negative integer.")
        loop = True

    else:

        #if input is negative continue the loop
        if(factorial <= -1):
            print("Error", user_input, "is not a valid non-negative integer.")
            loop = True

#Calculate Factorial

#factorial of 0 or 1 is always 1
if (factorial == 0 or factorial == 1):
    print(f"{factorial}{'!'}{' = '}{program_output}")

#else iterate through the integer to find the factorial
else:
    
    #program_ouput starts at 1, therefore if input is 3 (1*3*2 = 6)
    for index in range(factorial,1,-1):
        program_output = program_output * index

    print(f"{factorial}{'!'}{' = '}{program_output}")  
    






