'''
Author: Scott Field
Version : 1.0
Program Name: Get_Top_Three_Items_From_Sample_Data
Program Purpose: From sample data (dictionary) calculate the top three items priced in a shop, 
then display them in order from greatest quantity to smalles quantity.
'''

#Sample Data
dictionary =  {'Apple': 0.50, 'Banana': 0.20, 'Mango': 0.99, 'Coconut': 2.99, 'Pineapple': 3.99}

#Initialization
key_list = []
value_list = []
length = 0

#Obtain parallel lists containing the dictionaries keys and values
key_list = list(dictionary.keys())
value_list = list(dictionary.values())

length = len(key_list)

#Order the lists from greatest to least quantity

#Find the start value
for index in range(length):
    left_value = value_list[index]

    #Find the value the start  value will be tested against
    for inner_index in range(index+1,length):
        right_value = value_list[inner_index]

        #If the left value is less than the right value swap the values and keys
        if (left_value < right_value):
            #swap values
            value_list[index], value_list[inner_index] = value_list[inner_index], value_list[index]
            #swap keys
            key_list[index], key_list[inner_index] = key_list[inner_index], key_list[index]

#Print The Program Output (find the top 3 values and items)
num_values = 3

print(f"Input Dictionary: {dictionary}")
for index in range(num_values):
    print(f"{key_list[index]} {value_list[index]}")
