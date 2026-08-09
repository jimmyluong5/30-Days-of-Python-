#loops
#while loops, while a condition is going on do the following code
i = 0
#while i < 10:
   # print(i)
   # i= i+1

#break and continue
#use break when we would like to get out of a loop

while i < 10:
    print(i)
    i=i+1
    if i == 5:
        break

#here i = 5 right now
print("random string")
#with continue we can skip the current iteration at that condition like i==5
#while i < 10:
  #  print(i)
 #   i=i+1
  #  if i==6:
   #     print("lebron")
    #    continue #skips the next line of code and jumps back to the start (while i<10)
    #   i=i+1 #line won't execute

   



#for loop
#syntax: for iterator in sequence: 
    #do something


#example
for i in range(5): #this means i stops at the fifth index, from 0 - 4
    print('*' * i) #prints a triangle stops at 4 stars.

print('\n') #this just adds a space between the codes

numbers = [0, 1, 2, 3, 4, 5]
numbers2 = [1, 5, 6, 1, 6, 9, 4, 10]
for i in range(len(numbers)):
    #print(i)
    print(numbers[i]) #print the numbers

print('\n')

for i in range(len(numbers2)):
    print('lists:', numbers2[i])


#using for loop for tuples
print('\n' 'tuples:')


num = (1, 2, 3, 4, 5)
for i in num:
    print(i)

#for loop for dictionary
dict = {'name': 'Jimmy', 'age': 25, 'country': 'Canada', 'Language': 'Vietnamese'}

#for iterator in dictionary:
#looping through a dictionary gives you the key of the dictionary 

#for keys
for i in dict:
    print('\n', i) #or replace i with key


#for keys and values
for key, value in dict.items(): #turns this into a list of tuples
    print('\n', key, value) #we get both keys and its values 


it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for i in it_companies:
    print(i)


#using break and continue again\
for i in numbers:
    print(i)
    if i == 5:
        break

print('\n')

for i in numbers:
    print(i)
    if i == 5:
        continue
    if i != 5:
        print('The next number should be ', i+1)
    else:
        print('Loop finished')

print('We are outside the loop' '\n')


#range function
#used to return a list/array of numbers
#range(start,end,step) #range(0, 5, 1) , start at 0 and end at 5 (not including 5) and increments by 1

for i in range(0, 5):
    print(i)
    
print('\n')
for i in range(3): #starts at 0 and goes to 3 exclusive (not including 3)
    print(i)


#nested loops
#for x in y:
 #   for t in x:
#        print(t)

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {'street': 'Space street','zipcode': '02210'}
}

#loop through the list of skills
#for i in person:
    #if i == 'skills':
       # for j in person['skills']:
           # print(j)

#this is faster
for i in person['skills']:
    print(i)
    

#exercises

for i in range(0,8):
    print('#' * i)

i = 0
while i < 8:
    print('#' * i)
    i=i+1


for i in range(10, 0, -1):
    print(i, '\n')

for i in range (1):
    for j in range(0, 9):
        print('#' * 8)

    
for i in range(0, 11):
    print(i, 'x', i, '=', i**2)

#print the following using loops

lst=['Python', 'Numpy','Pandas','Django', 'Flask']
for i in lst:
    print(i)

#even numbers
for i in range(0,101):
    if (i % 2 ==0):
        print(i)

#odd numbers
for i in range(0, 101):
    if (i % 2 !=0):
        print(i)
    

#sum all numbers 
sum = 0
for i in range(0, 101):
    sum = sum+i

print('The sum of all numbers from 0-100 is:',sum)

sum_even, sum_odd = 0, 0
for i in range(0, 101):
    if (i % 2==0):
        sum_even = sum_even+i
    else:
        sum_odd = sum_odd+i

print('The sum of even numbers is:', sum_even)
print('The sum of odd numbers is:', sum_odd)


lst = ['banana', 'orange', 'mango', 'lemon'] 

for i in range(len(lst)-1, -1, -1):
    print(i)


