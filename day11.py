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
