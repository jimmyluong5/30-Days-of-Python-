#day 2 and this is built in functions of python 

import math #for the exercise to calculate the area of circle and shit



#printing a word
print("Hello, World")

#determining the length of characters in a string
word_len = len("Hello Lebron") #includes the spaces so it should be 12
print(word_len) #prints the number

#checks the data type of something
data_type=type ("Hello World") #this is a class string
print(data_type)

int_type = type(12)
print(int_type)

#changes the data type
x=str(10)
print(x)

y=str("10")
print(y)

#this takes in user input
#user_input = input("Enter your name: ")
#print(user_input) #this prints your name

#also has other functions such as min and max to find the min and max of number

min_val = min(12, 1, 3, 5, 13, 5)
print(min_val)


max_val = max(12, 1, 3, 5, 13, 5)
print(max_val)

#you can also do it with lists
max_val_list = max([12, 1, 2, 3, 5])
print(max_val_list)

#also summation 
sum_val=sum([1, 2, 3, 4, 5])
print(sum_val)



#variable -------
#must start with a letter or underscore character
#cannot start with a number
#alphabetical characters and underscores
#variable names are case sensitive

#valid variable names
#firstname
#lastname
#age
##country
#city
#first_name
#last_name
#capital_city
#_if # if we want to use reserved word as a variable
#year_2021
#year2021
#current_year_2021
#birth_year
#num1
#num2

#variable declaration
first_name = "Jimmy" #or you can use single quotations it doesn't matter
age = 25
is_tall=True #boolean
skills= ["HTML", "CSS", 'JS', 'Python'] #this is the list/array
person_info = {"firstname": 'Jimmy', 
            'lastname': 'Luong', 
            'country': 'Canada', 
            'city': 'Winnipeg'} #this is a dictionary, or a hashmap


#printing stuff, the print function has unlimited arguments as long as you separate them by '' and commas
print('Hello World')
print('Hello World', 'John Cena', 'Lebron James', '!')

#it can even print the length of a string
print(len('Lebron James'))


#declaring multiple variables in one line

first_name, last_name, country, age, is_single = 'Jimmy', 'Luong', 'Canada', '19', 'True'
print('First Name: ', first_name)
print('Last Name: ', first_name)
print('Country: ', country)
print('Age: ', age)
print('Single? ', is_single)

#getting user input
#first_name= input("What is your name: ")
#age = input("How old are you: ")

#print('Your name is:', first_name)
#print('Your age is:', age)

#exercises

#first_name_length = len(input ('What is your first name: '))
#print(first_name_length)

#last_name_length = len(input('What is your last name: '))
#print(last_name_length)

num_one = 5
num_two = 4

total = num_one + num_two
print(total)

diff = num_one-num_two
print(diff)

product = num_one*num_two
print(product)

remainder = num_one%num_two
print(remainder)

division = num_one/num_two
print(division)

exp = num_one ** num_two
print(exp)

floor_division = num_one //num_two
print(floor_division)

pi = math.pi

#calculate the area of a circle
radius = 40
area = int(radius)**2 *pi
print(area)

circumference = 2*pi*2*radius
print(circumference)

radius = input("What is the radius of the circle: ")
area = int(radius)**2 *pi
print(area)

