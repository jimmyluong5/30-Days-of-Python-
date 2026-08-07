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
    
#logical or statements
if a < 1 or a > 3:
    print ('A is less than 1 or greater than 3')


#exercise

#user_input = int(input('How old are you: '))
#if user_input >= 18:
#    print('You are old enough to drive.') and print('You are also old enough to vote.')
#else:
#    print('You are not old enough to drive or vote.')


person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
print(len(person['skills']))
if 'JavaScript' in person['skills']:
    print('He is a developer')

if 'skills' in person:
    first_index = 0
    middle_index =int( first_index + (len(person['skills'])-1)/2)
    print(middle_index)
    print(person['skills'][middle_index])

if 'skills' in person:
    if 'Python' in person['skills']:
        print('He is a Python developer')
if 'skills' in person:
    #convert skills to a set 
    skills = set(person['skills'])

    if {'JavaScript', 'React'} in skills:
        print("He is a front-end developer")
    elif {'Node', 'Python', 'MongoDB'} in skills:
        print('He is a back-end developer')
    elif {'React', 'Node', 'MongoDB'} in skills:
        print('He is a full-stack developer')
    else:
        print('unknown title')