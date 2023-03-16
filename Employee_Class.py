'''
Name: Employee_Class
Author: Scott Field
Date: 2/28/2023
Version: 1.0
Purpose: 

Write an Employee class that keeps data attributes for: Employee name and Employee number
Write a class named ProductionWorker that is a subclass of the Employee class. 
The ProductionWorker class should keep data attributes for the following information: Shift number (an integer, such as 1, 2, or 3) and Hourly pay rate

The workday is divided into two shifts: day and night. The shift attribute will hold an integer value representing the shift that the employee works. 
The day shift is shift 1 and the night shift is shift 2. Write the appropriate accessor and mutator methods for each class.

Once you have written the classes, 
write a program that creates an object of the ProductionWorker class and prompts the user to enter data for each of the object’s data attributes. 
Store the data in the object, then use the object's accessor methods to retrieve it and display it on the screen.
'''

class Employee():
    def __init__(self,name,number):
        self.name = name
        self.number = int(number)

    #Mutator Methods
    def assignName(self,newName):
        self.name = newName

    def assignNumber(self,newNumber):
        self.number = int(newNumber)

    #Accessor Methods
    def getName(self):
        return self.name
    
    def getNumber(self):
        return self.number

class ProductionWorker(Employee):
    def __init__(self,name,number,shift_number,hourly_pay):
        self.shift_number = int(shift_number)
        self.hourly_pay = float(hourly_pay)

        #gain the variable from employee
        Employee.__init__(self,name,number)

    #Mutator Methods
    def assignShift(self,newShift):
        self.shift = int(newShift)

    def assignPay(self,newPay):
        self.hourly_pay = float(newPay)

    #Accessor Methods
    def getShift(self):
        if self.shift == 1:
            return "Day"
        elif self.shift == 2:
            return "Night"
        #else return shift
        return self.shift

    def getPay(self):
        #set pay to 2 decimal places ($ system)
        format_pay = "{:.2f}".format(self.hourly_pay)
        return format_pay

#Input Validation Function
def validate(argument,type):
    #validate integers
    if (type == "int"):
        try:
            argument = int(argument)
        except:
            return False
        else:
            return True
    
    #validate floats
    else: #type == "float"
        try:
            argument = float(argument)
        except:
            return False
        else:
            return True
            

def main():
    #Initialize Variables
    user_input = ""
    name = ""
    id_number = 0
    shift_number = 0 #Shift Value Can be Either 1 or 2 representing day & night respectively (0 if shown represents an error)
    hourly_pay = 0.00
    
    #Initialize Classes
    ProductionGuy = ProductionWorker(name,id_number,shift_number,hourly_pay)

    #Welcome Message
    print("Please enter the requested data for employee information and the program will output the entered information in an organized format.\n")
    
    #Assign Values To Classes Using User Input

    #Assign User Input To Values
    user_input = input("Please enter the employee name.\n:")
    name = user_input

    #have to use name instead of ProductionGuy.getName() here or else I'd have to restructure the program
    user_input = input("Please enter the employee ("+name+") ID number.\n:")

    #Input Validation (Integer)
    while (validate(user_input,"int") == False):
        print("Error, Input Must Consist Of Numeric Characters")
        user_input = input("Please enter the employee ("+name+") ID number.\n:")
    #Once Input Is Valid Set Variable Equal To It
    id_number = int(user_input)

    #Add Values To Class
    ProductionGuy.assignName(name)
    ProductionGuy.assignNumber(id_number)

    #Assign User Input To Values
    user_input = input("Please enter the employee ("+ProductionGuy.getName()+") shift number\n(1 or 2):")
    shift_number = int(user_input)

    
    user_input = input("Please enter the employee ("+ProductionGuy.getName()+") hourly pay\n:")

    #Input Validation (Float)
    while (validate(user_input,"float") == False):
        print("Error, Input Must Consist Of Numeric Characters")
        user_input = input("Please enter the employee ("+ProductionGuy.getName()+") hourly pay\n:")
    #Once Input Is Valid Set Variable Equal To It
    hourly_pay = float(user_input)

    #Add Values To Class
    ProductionGuy.assignShift(shift_number)
    ProductionGuy.assignPay(hourly_pay)

    #Print Class Attributes Using Accessor Methods
    print("\nName:", ProductionGuy.getName())
    print("Id Number:", ProductionGuy.getNumber())
    print("Shift:", ProductionGuy.getShift())
    print("Hourly Pay:", ProductionGuy.getPay())



#main loop
if __name__ == "__main__":
    main()

