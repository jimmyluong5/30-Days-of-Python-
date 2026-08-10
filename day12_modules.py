#modules
#modules are files containing a set of code or 
# a set of functions that can be included to an application

#a module could be a file containing a single variable, a function or a big code base

#to create a module, we write our codes in a python script and we save it as a .py file

import mymodule
from mymodule import generate_name
print(mymodule.generate_name("jimmy", "luong"))
print(generate_name('Lebron', 'James'))

#we can also change the name of the file when we import the module

from mymodule import sum_two_numbers as total
print(total(10,10))

#we can also import built in modules such as the Operating Systems module
#Some of the common built-in modules: math, datetime, os,sys, random, statistics, collections, json,re

#os module, makes it possible to perform many operating system tasks, it provides
#functions for creating, changing current working directory (folders), removing directories (folders), listing files and many more
#directory = folders
#import the module
import os

#creating a directory
#os.mkdir("test")

#change directory path
#os.chdir('path') #copy and paste the path here

#get the working directory path here
#os.getcwd()

#removing a directory (folder)
#os.rmdir('test')




#sys module
import sys
#provides functions and variables used to manipulate different parts of the python runtime environment
#runtime environment is the software that runs the python code
#Functions sys.argv returns a list of command line arguments passed to a Python script
#the item at index 0 is always the name of the script, at index 1 is the argument
#passed from the command line 

#argv stands for argument values

#imagine you type this into the terminal 
#python recipe.py bake 350
#sys.argv[0] = recipe.py
#sys.argv[1] = 'bake'
#sys.argv[2] = '350'

#math module, contains functions for mathematical operations

#user_name = sys.argv[1] #get the first word after the script name
#age = sys.argv[2] #get the second word after the script name
#print(user_name)
#print(age)


#statistics module

from statistics import *
age = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(age))
print(median(age))
print(mode(age))
print(stdev(age))

#math module
import math
print(math.pi)
print(math.sqrt(4))
print(math.pow(2,3)) #2^3
print(math.floor(9.81)) #9
print(math.ceil(9.81)) #10
print(math.factorial(9)) #9!
print(math.log10(100)) #2


from math import pi #we can now use the pi value
print(pi)

#string module

import string
print(string.ascii_letters) #a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z
print(string.digits) #0, 1, 2, 3, 4, 5, 6, 7, 8, 9
print(string.punctuation) #!, @, #, $, %, ^, &, *, (, ), -, _, =, +, [, ], {, }, |, \, :, ;, ', ", <, >, ,, ., /

#random module
from random import random, randint

print(random()) #get a random float between 0 and 1
print(randint(1, 25)) #get a random integer between 1 and 25


#exercises

#function that generates a 6 digit random user id

def random_user_id():
    from random import random, randint
    user_id = randint(0, 999999)
    return user_id
print(random_user_id())


def user_id_gen_by_user():
    from random import choice
    #we will use the choice function to pick a random element from the pool of characters, 
    #it will append a random letter/digit to the existing user_id
   
    #ask the user for the number of characters of their desired ID
    num_char = int(input('Enter the number of characters of your desired ID: '))
    #ask the user for the number of IDs they want to generate
    num_id = int(input('Enter the number of IDs you want to generate: '))


    #this is the pool of letters and digits to choose from
    characters = string.digits+string.ascii_letters

    #nested for loop
    #outer loop is based on the number ids that we need to generate
    #inner loop is the actual user_id we generate which we will append one letter at a time

    for i in range(num_id):
      #start with an empty string of the user_id
      user_id = ''
      for j in range(num_char):
        user_id += choice(characters)
      #print the user id
      print(user_id) #prints the completed user_id after the desired length

#user_id_gen_by_user()

#3

def rgb_color_gen():
    #it will print 3 random numbers from 0 to 255 each
    #create an array of the numbers
    rgb = list() #create the empty set of numbers
    for i in range(3):
        rgb.append(randint(0,255))
    print('rgb',rgb) #print rgb 

print(rgb_color_gen())





                