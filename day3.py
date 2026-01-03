#day 3 - operators

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
