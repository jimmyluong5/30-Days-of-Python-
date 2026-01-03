#day 1 - intro to python, introduction to the data types

#printing numbers
print (1+3) # addition +
print(3-2) # subtraction

print(3*2) #multiplication
print(3/2) #integer division

print(3**2) #exponent
print(3%2) #modulus operator

#checking data types
print( type(10)) #this should be an integer

print(type(3.14)) #float
print(type((1+3j))) #complex type

print(type("Jimmy")) #string

print(type([1, 2, 3, 4])) #this is a list/array
print(type({"name": "Lebron"})) #this is a dictionary or hashmap

print(type({9.8, 1.2, 3})) #this is a set, which is a data structure that stores a collection of items (unordered, mutable and unique and allow for duplicates)
#immutable objects 
#cannot be modified in place after creation, python doesnt change the original but instead creates a brand new object in memory with the new value and updates the variable to point to a new location
#eg ints, floats, complex, str, tuple, booleans

#mutable objects can be modified in place without creating a new object in memory
#lists, dictionaries, sets, and user-defined classes (which are structs)
print(type((9.8, 3.14, 2.7)))    # Tuple (stores data but is immutable)
print(type(3 == 3))              # Bool
print(type(3 >= 3))              # Bool