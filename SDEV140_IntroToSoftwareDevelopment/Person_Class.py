'''
Name: Person_Class
Author: Scott Field
Date: 2/28/2023
Version: 1.0
Purpose: Write a class named Person with data attributes for a person's name, address, and telephone number. 
Next, write a class named Customer that is a subclass of the Person class. 
The Customer class should have a data attribute for a customer number,
and a Boolean data attribute indicating whether the customer wishes to be on a mailing list. 
Demonstrate an instance of the Customer class in a simple program
'''

#Create Person Class
class Person:
    #define class on initialization
    def __init__(self,name,address,phone_number):
        self.name = name #string containing name
        self.address = address #string containing address
        self.phone_number = phone_number #integer containing phone_number

    #define output when class is printed
    def __str__(self):
        #Note: __str__ must return a string not print them
        return "Name: " + self.name + "\nAddress: " + self.address + "\nPhone Number: " + self.phone_number

#Create Customer Class
class Customer(Person):
    #define class on initialization
    def __init__(self,name,address,phone_number,customer_id,mailing_list):
        #add new data values to customer
        self.customer_id = customer_id  #integer containing customer ID number
        self.mailing_list = mailing_list #boolean containing if customer wishes to be on mailing list

        #call superclass __init__method
        Person.__init__(self,name,address,phone_number)
        #gain the init method from parent class (Person) in order to gain instance variables
        
     
    #override the __str__ method from Person
    def __str__(self):
        #Note: __str__ must return a string not print them
        return Person.__str__(self) + "\nCustomer ID#: " + str(self.customer_id) +"\nCustomer Consents To Be On Mailing List: " + str(self.mailing_list)
        


#Main Loop Testing Classes
def main():
    #Welcome Message
    print("Please enter a persons prompted information, and this program will output the information entered in an organized format.")

    #Initialization
    user_input = ""
    name = ""
    address = ""
    phone_number = ""
    customer_id = 0
    mailing_list = False

    #used for input validation
    validated = False

    #used to check if phone number contains numbers
    numbers = "0123456789"

    #Get Input From User For Person Class
    user_input = input("Please enter the name of the person\n:")
    name = user_input

    user_input = input("Please enter the address of : "+name+"\n:")
    address = user_input

    #Input Validation Loop For Phone Number Entry
    while not validated:
        user_input = input("Please enter the phone number of : "+name+"\n:")
        phone_number = user_input
        for i in range(len(phone_number)):
            if phone_number[i] not in numbers:
                print("Error phone number can only consist of 10 numeric characters.")
            elif len(phone_number)==10:
                validated = True
            else:
                print("Error phone number can only consist of 10 numeric characters.")
                #exit validation upon finding incorrect phone number character
                break

    #Get Input From User For Customer Class

    #Input Validation Loop For Custmer ID Entry
    validated = False
    while not validated:
        user_input = input("Please enter the Customer ID# of : "+name+" in numeric form\n:")
        try:
            customer_id = int(user_input)
        except:
            print("Value Error, customer id must consist of only numeric characters")
        else:
            validated = True

    #Input Validation Loop For Mailing List Entry
    validated = False
    while not validated:
        user_input = input("Does the customer: "+name+" wish to be on a mailing list?\n(True or False):")
        if (user_input == "True"):
            mailing_list = True
            validated = True
        elif(user_input =="False"):
            mailing_list = False
            validated = True
        else:
            print("Value Error, mailing list only accepts the value: True or the value: False")
            
        
    #Demonstrate Inheritance Between Classes
    newPerson = Person(name,address,phone_number)
    newCustomer = Customer(newPerson.name,newPerson.address,newPerson.phone_number,customer_id,mailing_list)



    print("Person Class Outputs:\n\n",newPerson)
    print("\nCustomer Class Outputs:\n\n",newCustomer)

    
#Main Loop
if __name__ =="__main__":
    main()


