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

