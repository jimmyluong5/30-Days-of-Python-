#day 3 - operators

import math

#such as True and False
#must be capitalized


# Arithmetic Operations in Python
# Integers

print('Addition', 1+3)
print('Subtraction', 1-2)
print('Multiplication', 2*3)
print('Division', 4/2) #division in python gives a floating point number
print('Division without the remainder', 7//2) #gives you the float of the value so 3.5 -> 3
print('Modulus', 3%2) #gives the remainder
print('Exponentiation', 2**2)

# Floating numbers
print('Floating Point Number, PI', 3.14)
print('Floating Point Number, gravity', 9.81)

# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j))

# Declaring the variable at the top first

a = 3 # a is a variable name and 3 is an integer data type
b = 2 # b is a variable name and 3 is an integer data type

# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# I should have used sum instead of total but sum is a built-in function - try to avoid overriding built-in functions
print(total) # if you do not label your print with some string, you never know where the result is coming from
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)


#calculate area of circle
radius = 10
pi = math.pi
area_circle = pi * radius**2
print('The area of the circle is:',area_circle, 'units^2')

#calculate the area of the rectangle
length = 10
width = 5
print('The area of the rectangle is:',length*width, 'units')

#calcluate the weight of the object
mass = 75
gravity = 9.81
weight = mass*gravity
print('The weight of this object is:', weight, 'N') #prints the weight and the unit beside

print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False


# Comparing something gives either a True or False

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)


#other comparsion types such as "is, is not, in, not in "

print('1 is 2', 1 is 2) #should be False
print('1 is not 2', 1 is not 2) #should be True it also works with strings

print('L in Lebron', 'L' in 'Lebron') #True
print('J not in Lebron', 'J' in 'Lebron') #False


print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False
