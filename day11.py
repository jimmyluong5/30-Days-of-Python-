#functions
#declaring a function
#def function_name(inputs)
#call function 

#example

def function_name():
    print('Hello World')

function_name()

#function without parameters
def function_greeting():
    print('Hello, my name is Jimmy')

function_greeting()

#function returning a value 
def generate_full_name():
    first_name = 'Lebron'
    last_name = 'James'
    full_name = first_name + ' ' + last_name
    return full_name #so when we call it it will give back this

name=generate_full_name()
print(name)

#adding two numbers
def sum():
    a = 2
    b = 3
    c = a+b
    return c

answer=sum()
print(answer)

#with parameters
def sum_parameters(a,b):
    c = a+b
    return c

answer = sum_parameters(1,2)
print(answer)

print('\n')

#or if we do this, the order of the parameters doesn't matter as long as we explicitly state para_2 = x, para_1 = y and vice versa
#or just input the parameters like normal
answer = sum_parameters(b = 2, a = 4)
print(answer)




#sum of numbers (n)
def sum_all_num(n):
    sum = 0
    for i in range(n+1): #goes from 0 to n+1 because we need to include the nth number
        sum +=i
    return sum

print(sum_all_num(100)) #should get 5050

def generate_full_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name

print(generate_full_name('Steph', 'Curry'))


#returning a boolean example
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
def is_odd(num):
    if num % 2 !=0:
        return True
    else:
        return False

print(is_odd(3))
print(is_even(2))

#we can make a function that finds all the even numbers and places them into an array by iterating from 0 to n+1 to include n
def sort_numbers(num):
    #first create an empty list
    even_numbers = []
    odd_numbers = []
    for i in range(num+1):
        #even numbers
        if i % 2 == 0:
            even_numbers.append(i) #we are adding the even numbers to the list
        else:
            odd_numbers.append(i) #where i is the iterating variable but contains the numbers at that index
    return even_numbers, odd_numbers

print(sort_numbers(10))

#if we don't know the number of arguments to pass to the function then we can use a pointer?
def sum_all_num(*n):
    total = 0 
    for i in n:
        total +=i
    return total

answer = sum_all_num(1,2)
print(answer) #3


#dictionary unpacking which means we can access the key-value pairs in a dictionary
def greet(name, location):

    #print a greeting
    print('Hi there', name, 'how is the weather in', location)

#call the function
#greet(name = 'Lebron', location = 'Canada')

print('\n')

#or create a dictionary with the same parameters
dict = {'name': 'Lebron', 'location': 'Canada'}

#unpack the dictionary
greet(**dict)


#exercises

def add_two_numbers(a,b):
    c = a+b
    return c


def area_circle(radius):
    return 3.14 * radius**2

def add_all_nums(*numbers):
    sum = 0
    for i in numbers:
        sum +=i
    return sum

def convert_celsius_to_fahrenheit(celsius_temp):
    farenheit = (celsius_temp* 9/5) + 32
    return farenheit

def check_season(month):
    if month in ['September', 'October', 'November']:
        return 'Autumn'
    elif month in ['March', 'April', 'May']:
        return 'Spring'
    elif month in ['June', 'July', 'August']:
        return 'Summer'
    else:
        return 'Winter'
print(check_season('September'))

#6 write function that returns the slope of a linear equation
def calculate_slope(x1,y1, x2, y2):
    slope = (y2-y1)/(x2-x1)
    return slope

def quad_eqn(a,b,c):
    discrim = b**2 - 4*a*c

    if discrim > 0: #real roots
        x1 = (-b + discrim**0.5)/2*a
        x2 = (-b - discrim**0.5)/2*a
        return x1, x2
    elif discrim == 0:
        x = -b/2*a
        return x
    else:
        print('No real roots')


print(quad_eqn(1,5,6))

def print_list(lst):
    for i in lst:
        print(i)

print_list([1,2,3,4])

#reverse list
def reverse_list(lst):
    i = 0
    j = len(lst)-1

    while i < j:
        #swap the elements
        lst[i] = lst[j]
        lst[j] = lst[i]
        i +=1
        j -=1
    return lst

print(reverse_list([1,2,3,4]))

def capitalize_list_items(lst):
    #just need to capitalize the items, then return the new list
    #use strings for this
    for word in lst:
        word = word.upper()
    return lst

print(capitalize_list_items(['lebron']))

def add_item(lst, item):
    lst.append(item)
    return lst

print(add_item(['lebron'], 'James'))

def remove_item(lst):
    lst.pop(1)
    return lst

print(remove_item(['Lebron', 'James']))

def sum_of_numbers(n):
    sum = 0
    for i in range(n+1):
        sum = sum + i
    return sum
print(sum_of_numbers(100)) #should be 5050

def sum_of_odds(num):
    total = 0
    for i in range(num+1):
        if i % 2 != 0:
            total +=i
    return total

print(sum_of_odds(100)) #should be 2500

def sum_of_evens(num):
    sum = 0
    for i in range(num+1):
        if i%2==0:
            sum+=i
    return sum
print(sum_of_evens(100)) #2550


def evens_and_odds(n):
    odd_count = 0
    even_count = 0
    for i in range(n+1):
        if i %2 == 0:
            even_count+=1
        else:
            odd_count +=1
    return even_count, odd_count

print(evens_and_odds(100))