'''
Author: Scott Field
Version: 1.0
Program Name: Display_Sales_Tax
Program Purpose: From an inputed total sales float, output the county sales tax, state sales tax, and total sales tax (county + state)
'''

#Welcome Message
print("Please enter the total sales for the month, and the program will output the county sales tax, state sales tax, and total sales tax for the entered total.\n")

#Initialization
county_tax = 0.025
state_tax = 0.05
total_tax = 0.0
user_input = ""
loop = True
number = 0.0

#User Input & Input Validation
while (loop):
    user_input = input("Please enter the total sales for the month in numeric form, the program will then output the county, state and total taxes on the sales.\n:")

    #attempt to convert input to integer
    try:

        number = float(user_input)
        loop = False

    except:

        #if input is not a number continue the loop
        print("Error", "'", user_input , "'" , "is not a number, this loop will repeat until a valid number >= 0 is entered.")
        loop = True

    #Logically Total Sales Cannot Be Less Than 0
    if number < 0:
        print("Error the entered sales total:", "'", user_input , "'" , " must be >= 0 , this loop will repeat until a valid number >= 0 is entered.")
        loop = True

#Calculate The Amounts of The Taxes
county_tax = number * county_tax
state_tax = number * state_tax
total_tax = county_tax + state_tax

#Print the tax amounts to 2 decimal places
print(f"The county sales tax for {number:.2f} is: {(county_tax):.2f}")
print(f"The state  sales tax for {number:.2f} is: {(state_tax):.2f}")
print(f"The total  sales tax for {number:.2f} is: {(total_tax):.2f}")