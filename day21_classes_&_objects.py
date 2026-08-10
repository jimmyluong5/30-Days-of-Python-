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

#self is like the ptr in C, it gives you access to the object and its attributes.

#example
#self.name is equivalent to ptr->name
#or
#self.age = age is equivalent to ptr->age=age but self is just an object reference not ptr
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

#object methods
#objects can have methods, methods are functions that belong to the object or class. 
#methods is a function defined in the class 
#and operates on instances of that class/type of variable(objects)

class Person:
    def __init__ (self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
    
    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'

p = Person('Lebron', 'James', 42, 'USA', 'Los Angeles')
print(p.person_info())

class Person:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'

p1 = Person() #instead of inputting all the values, we can just use the default values
print(p1.person_info())
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())

#method of modify class default values
#lets say we want to add a new method which will append a new skill to the class.


class Person:
    def __init__(self, firstname='Lebron', lastname='James', age=42, country='USA', city='Los Angeles'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city 
          #create the new class attribute
          self.skills = [] #empty list of skills

    #this is a method
    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'
    def add_skill(self, skill):
        self.skills.append(skill)

#creating objects
p1 = Person()
print(p1.person_info())

#adding skills to object p1
p1.add_skill('HTML')
p1.add_skill('JavaScript')

#creating object 2
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
p2.add_skill('Python')
p2.add_skill('C')
print(p2.person_info())
#print the skills of each object
print(p1.skills)
print(p2.skills)

#inheritance we can reuse the parent code. 
#like a child can inherit attributes and methods from a parent, a class can inherit from another class
#we create a new class that inherits from the Person class
#like Parent -> Child, this Child node inherits all of the same attributes and methods from the parent
# syntax -> class ChildClassName(ParentClassName):
    #code

class Student(Person): #this Student class will now include all of the methods and attributes
    pass 

s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo')

print(s1.person_info())
print(s2.person_info())

s1.add_skill('programming')
s1.add_skill('react')
s2.add_skill('JavaScript')
s2.add_skill('Angular')

print(s1.skills)
print(s2.skills)

#exercise
class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.income = {}
        self.expenses = {}

    def total_income(self):
        total = 0
        #just sum up all the incomes in the dictionary
        for i in self.income.values(): #it must be the key values not the key itself.
            total += i
        return total
    
    def total_expenses(self):
        total = 0
        for i in self.expenses.values():
            total += i
        return total

    def acc_balance(self):
        #call the methods and calculate the difference
        return self.total_income()-self.total_expenses()

    def add_income(self, description, amount):
        self.income[description] = amount
    
    def add_expense(self, description, amount):
        self.expenses[description] = amount #hashmap, description is the key, amount is key value.


    def account_info(self):
        return f'{self.firstname} {self.lastname} has a total income of ${self.total_income()}, total expenses of ${self.total_expenses()}, and an account balance of ${self.acc_balance()}.'


# Example usage:
p = PersonAccount('Lebron', 'James')
p.add_income('Salary', 50000)
p.add_income('Bonus', 10000)
p.add_expense('Rent', 4000)
p.add_expense('Food', 1000)

print(p.account_info())
