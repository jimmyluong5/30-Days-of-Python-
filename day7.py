#creating a set

#set_name = set()
#or set_name = {'item1', 'item2'}

#sets are unordered and unindexed collection of items

fruits = {'apples', 'bananas', 'oranges', 'mangoes'}

#set length
print(len(fruits))

#later we use loops and we can access items in sets

#checking an item
does_exist = 'apples' in fruits
print(does_exist)

#adding items to sets
fruits = {'apples', 'bananas', 'oranges', 'mangoes'}
fruits.add('peaches')
print(fruits)

#adding multiple items to a set, using the update condition 
fruits = {'apples', 'bananas', 'oranges', 'mangoes'}
fruits.update(['lemons', 'grapes', 'dragonfruit' ])
print(fruits)

#we can also remove items using .remove (using a specific item) or .pop() - this one removes a random item in the set cuz theres no index

fruits.remove ('mangoes')
print(fruits)

fruits.pop() #removes a random item and returns that removed(Random) item.
print(fruits)

#clearing a set
fruits.clear()
fruits = {'lebron'}
print(fruits)

#deleting a set
del fruits
#print(fruits) #should get error message

#converting list to set
list = ['lebron']
print(list)
list = set(list)
print(list)

#joining sets (using union or update)

set1 = {'lebron', 'jordan'}
set2 = {'durant', 'curry'}
set3 = set1.union(set2) #combining set2 to set1
print(set3)

set1.update(set2) #combining set2 to set1
print(set1)

#finding intersection items
#returns a set of items that are in both sets

set1 = {'lebron', 'jordan', 'kobe'}
set2 = {'lebron', 'curry','kobe'}
set3 = set1.intersection(set2)
print(set3)

#checking subset and superset
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True, checking if st2 is subset of st1
st1.issuperset(st2) # True, checking if st1 is superset of st2
print(st2.issubset(st1)) # True, checking if st2 is subset of st1
print(st1.issuperset(st2)) # True, checking if st1 is superset of st2

#checking the difference between two sets, returns the difference between two sets
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set() : st2 - st1
st1.difference(st2) # {'item1', 'item4'} => st1\st2  : st2 - st1
print(st2.difference(st1)) #empty set()
print(st1.difference(st2)) # {'item1', 'item4'}

#find the symmetric difference between two sets
#returns a set that contains all items from both sets, except items that are present in both sets
result = st2.symmetric_difference(st1)
print(result) #{'item4', 'item1'}

#if the sets do not share common items, then they are disjoint sets
st2.isdisjoint(st1) #is st1 disjoint with st2?
print(st2.isdisjoint(st1)) #its False because they share items

#exercises
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)

it_companies.update(['Netflix', 'Hulu', 'Disney+'])
print(it_companies)

it_companies.pop()
print(it_companies)

#exercise 2
A.union(B)
print(A)

result=A.intersection(B)
print(result)

result = A.issubset(B)
print(result)

result = A.isdisjoint(B)
print(result)

result = A.symmetric_difference(B)
print(result)


print(len(A))
A = set(A)
print(len(A))

