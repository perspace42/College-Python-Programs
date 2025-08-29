'''
Name: Tkinter_Temperature_Conversion
Author: Scott Field
Date: 2/22/2023
Version: 3.0
Purpose: Using Tkinter, Take User Input, Then Convert Celsius Temperature Inputed To Farenheit or Vice Versa
'''

#Import Tkinter
from tkinter import *
from tkinter import ttk  
from tkinter import messagebox 


#Functions

#Input Validation Function
def validate(user_input):
    decimal = 0.0
    #Input Validation
    try:
        decimal = float(user_input)
    except:
        #Create Error Message
        messagebox.showerror("Input Validation Error"," Input must Be In Integer or Decimal Form. This Error Will Repeat Until Valid Input Is Entered")
        #Input is Invalid
        return False
    else:
        #Input is Valid
        return True

#Temperature Conversion Function
def convertTo(unit):
    #Initialize Variables
    temperature = 0.0
    calculation = 0.0
    #It is important to set user_input = entry.get() as entered_text.get() will only return the default text
    user_input = entry.get()

    #Input Validation
    if validate(user_input) == True:
        temperature = float(user_input)

         #Convert Temperature To Farenheit
        if unit == 'F':
            #Perform Calculation
            calculation = (9/5) * temperature + 32
            
            #Output Conversion To Label
            output_label.config(text = (str(user_input) + "°C = " + str(calculation) + "°F"))

        #Convert Temperature to Celsius
        else:
            #Perform Calculation
            calculation = ((5*temperature) - 160)/9
            
            #Output Conversion To Label
            output_label.config(text = (str(user_input) + "°F = " + str(calculation) + "°C"))
    else:
        #Clear invalid input
        entry.delete(0,END)
        


#Create and Populate Window
root = Tk()
root.title("Temperature Converter")


#Turn Text Value Into Variable class
entered_text = StringVar()
entered_text.set("Enter a Temperature To Be Converted:")

#Turn Label Value Into Variable class
output_text = StringVar()
output_text = "Conversion Displayed Here:"

#Create the Text Entry
entry = ttk.Entry(root, width = 40)
entry.grid(row = 1, column = 2 )
entry.insert(0, entered_text.get())

#Set Event To Clear Text Entry On Mouse 1 Click
def click(event):
    #set state
    entry.configure(state = "normal")
    #remove text
    entry.delete(0,END)
    #unbind event after click
    entry.unbind('<Button-1>', mouse_clicked)

#Set Buttons
cel_button = ttk.Button(root, text = "Convert To Celsius", command = lambda: convertTo('C'))
far_button = ttk.Button(root, text = "Convert To Farenheit", command = lambda: convertTo('F'))

#Set ReadOnly Entry
output_label = ttk.Label(root, text = output_text)

#Position Buttons On Grid
cel_button.grid(row = 2, column = 1)
far_button.grid(row = 2, column = 3)

#Position Label On Grid
output_label.grid(row= 3, column = 2)

#Main Loop

#bind mouse click to clear text box
mouse_clicked = entry.bind('<Button-1>', click)

#Set Window To Loop
root.mainloop()