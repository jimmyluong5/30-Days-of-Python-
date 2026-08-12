#exception handling
#python uses try and except to handle errors
#the try block lets you test a block of code for errors
#the except block lets you handle the error
#the else block lets you execute code when there is no error
#the finally block lets you execute code whether there is an error or not

""" Purpose: Prevents application crashes when serious or external errors occur (e.g., bad inputs, missing files, I/O failures).
Action: Catches the exception, logs a descriptive error message, and shuts down or recovers cleanly.
Benefit: Improves application reliability and debuggability. """

#try - run this code
#except - execute this code if there is an error
#else - execute this code if there is no error
#finally - execute this code no matter what

#code example snippet
""" try: 
    #code that might raise an error 
    pass
except:
    #code to run if an error occurs 
    pass
else: 
    #code to run if no error occurs
    pass
finally: 
    #code that always runs
    pass 
""" 



"""  try: 
    print(10 + '5')
except:
    print('Something went wrong')
    """


""" try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except:
    print('Something went wrong') """


#we can try and determine the problem using excepts

try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occur')
except ValueError:
    print('Value error occur')
except ZeroDivisionError:
    print('zero division error occur')
else:
    print('I usually run with the try block')
finally:
    print('I always run.')




