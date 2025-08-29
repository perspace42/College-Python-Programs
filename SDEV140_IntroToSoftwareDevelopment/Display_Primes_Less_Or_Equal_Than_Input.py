'''
Author: Scott Field
Version : 1.0
Program Name: Display_Primes_Less_Or_Equal_Than_Input
Program Purpose: Accept an integer input greater than 1, 
then display all of the prime numbers that are less than or equal to the number entered
'''
#Functions

def isPrime(number):
    decimal = float(number)
    
    #Divide input by range (2 to input-1) to check if it is prime
    for index in range (2,number):
        #If a numbers floor division is equal to its regular division then it isn't prime
        if (decimal / index == decimal // index):
            return False 

    #If a number never evenly divides it must be prime
    return True

def createList(length):
    list = []
    for index in range(2,length + 1):
        list.append(index)

    return list

#Welcome Message
print("Please input a positive integer greater than 1, and the program will display of all prime numbers that are less than or equal to the number entered.\n")

#Initialization
prime_list = []
user_input = ""
number = 0
test_number = 0
loop = True

#User Input & Input Validation
while (loop):
    user_input = input("Please enter an integer greater than 1 for the program to display all primes less than or equal to that integer.\n:")

    #attempt to convert input to integer
    try:

        number = int(user_input)
        loop = False

    except:

        #if input is not a number continue the loop
        print("Error", "'", user_input , "'" , "is not a valid integer, this loop will repeat until a positive integer is entered that is greater than 1.")
        loop = True

    else:

        #if input is less than or equal to 1 continue the loop
        if(number <= 1):
            print("Error", user_input, "is < 1, this loop will repeat until a positive integer is entered that is greater than 1.")
            loop = True

#Create List
prime_list = createList(number)
output_list = []

#Step through prime list, checking if each number within is prime.
for index in range(len(prime_list)):
    test_number = prime_list[index]
    #If a number in the list is prime add it to the output
    if (isPrime(test_number)):
        output_list.append(test_number)

#Output data to user.    
print(f"The prime numbers <= {number} are : {output_list}.")
    

