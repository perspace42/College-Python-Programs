'''
Author: Scott Field
Version: 1.0
Date: 1/24/2022
Program Name: Color Mixer
Purpose: Calculate the output of mixing red, blue and yellow after prompting the user for two primary colors
'''
#Welcome Message
print("This program will return the result of mixing two primary colors (red, blue, yellow) entered by the user.\n")

#Initialize Variables
user_input = ""
first_color = ""
second_color = ""

#Input Validation
while (first_color == ""):
  user_input = input("Please enter the first primary color (red, blue, yellow).\n:")
  user_input = user_input.lower()

  #Input Validation Test
  if (user_input == "red" or user_input == "blue" or user_input == "yellow"):
    first_color = user_input

  #Error Message If Input Is Invalid
  else:
    print("Error: ", user_input , "is not an valid primary color. this loop will repeat until a valid primary color is entered.")

#2nd Input Validation
while (second_color == ""):
  user_input = input("Please enter the second primary color (red, blue, yellow).\n:")
  user_input = user_input.lower()

  #Input Validation Test
  if (user_input == "red" or user_input == "blue" or user_input == "yellow"):
    second_color = user_input
    
  #Error Message If Input Is Invalid
  else:
    print("Error: ", user_input , "is not an valid primary color. this loop will repeat until a valid primary color is entered.")

#Calculate then Output the Produced Color

#If both are the same, same and same = same
if (first_color == second_color):
  print("\nThe color" , first_color , "mixed with" , second_color , "creates:" , first_color)

#Red and Blue = Purple
elif((first_color == "red" or second_color == "red") and (first_color == "blue" or second_color == "blue")):
  print("\nThe color" , first_color , "mixed with" , second_color , "creates:" , "purple")

#Red and Yellow = Orange
elif((first_color == "red" or second_color == "red") and (first_color == "yellow" or second_color == "yellow")):
  print("\nThe color" , first_color , "mixed with" , second_color , "creates:" , "orange")

#Blue and Yellow = Green (last possiblilty)
else:
  print("\nThe color" , first_color , "mixed with" , second_color , "creates:" , "green")





