#python is a object orientated programming language. everything in python is an object
#numbers,strings, list, dictionary like anything is an object used in a program
#of a corresponding built-in class.

#we create classes to create objects
#like species and individual organisms.

#a class is like a object constructor or 'blueprint' for creating objects.
#We instantiate a class to create an object.

#so basically the class is the variable type, and the object is the actual value a variable of that class

#example 
num = 10, #num is of class integer, 10 is the object, the object's value is 10.
# num  → variable/name
# int  → class/type
# 10   → object of class int
# 10   → the object's value

#this is the same thing as structures in C, where you define your own class or variable type

#to create a class, we need the key word 'class' followed by the name and colon
#usually class names are written in CamelCase format
#example

#class ClassName:
    #code


class Person:
    pass
print(Person) #<class '__main__.Person'>

#creating an object
#we can create an object by calling the class as a function
#syntax → objectName = ClassName()
p = Person()
print(p) #<__main__.Person object at 0x000001DA96685E90>

#class constructor 
#a class without a constructor is not useful
#we use the constructor function 
class Person:
    def __init__(self, name): #used to give the new object its starting attributes
        #self allows to attach parameter to the class
        self.name = name 

p = Person("Jimmy")
print(p.name) #to access the object, you need to do p.name or p.attribute.AttributeError


#we can add more attributes to the constructor function
class Person:
    def __init__ (self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

#creating one node/object.
p = Person('Jimmy', 'Luong', '20', 'Canada', 'Vancouver')
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)
#class method
#a class method is a method that is called on a class, not an object    