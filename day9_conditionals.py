#conditionals, if else statements

#syntax
#if statement:
    #indent then write stuff here, only the indented section is part of the if statement
a=2
if a > 2:
    print('Lebron James')
elif a == 2:
    print('Booker')
else:
    print('Curry')


#short hand form 
#code if condition else code
a=2
print('Lebron James') if a > 3 else print('Lillard')


#nested if statements
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

#if condition and logical operators
a=4
if a > 3 and a < 10:
    print('A is between 3 and 10')
else:
    print('A is not between 3 and 10')
    


