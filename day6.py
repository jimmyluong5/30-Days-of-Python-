#tuples - collection of data that are inmutable, which means you cannot change the values
#which is ordered

#tuples are (), lists are []

tuples = () #empty tuple

tuples = tuple() #empty tuple

#tuples can hold different data types 
tuples = ('banana','apple',3,4,True,3.14)
print(tuples)


print(tuples[0])

#tuple len
print(len(tuples))

#changing tuples to lists
tuples = list(tuples)
print(tuples)

#changing lists to tuples
list = ['lebron', 'curry', 'booker']
list = tuple(list)
print(list)