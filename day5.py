#day 5 - lists
#a list is just an array from other programming languages
#but it can hold different data types in one list
#lists are mutable, meaning you can change the values in the list
#it can hold strings, ints, floats, etc.

#collection of data, that is mutable and ordered


#we can create a list several ways, this is just an array
#you can do it by using [] or ()

arr = [] #empty list

#or 
arr1 = ()

#or 
empty_list = list()

#list of fruits
fruits = ['Apples', 'Blueberries', 'Oranges', 'Mangoes','Lemon', 'Pineapple','Watermelons','Pears']

#len(length) is used to find the number of items in a list
print(len(fruits)) #4

#or print the fruits itself
print('Fruits', fruits)


#lists can also have different data types in it 
lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}] # list containing different data types


#we can access each element in the list/array using its index from 0 to n 
print(fruits[0]) #this will be the apples

#determine the last index
last_index = len(fruits)-1
print(last_index)
print(fruits[last_index])

#negative indexing
#more negative means its the start, more positive means its closer to the end of the array
print(fruits[-4]) #first item in the array
print(fruits[-1]) #last item in the array

#unpacking list items
lst = ['item1','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)
print(second_item)
print(third_item)
print(rest)

first, second, *rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)          # 1
print(second)         # 2
#print(third)          # 3
print(rest)           # [4,5,6,7,8,9]
print(tenth)          # 10


#slicing items from a list
#for positive indexing: we can specify a range of positive indices by specifying the start, end and step
#the return value will be a new list 
#default values start = 0, end = len(array)-1, step = 1

all_fruits=fruits[0:4] #prints all the fruits starting from 0 to 4
print(all_fruits)

all_fruits1 = fruits[0:] #if we don't specify where to stop, it just takes the rest
print(all_fruits1)

all_fruits2 = fruits[1:2] #this will return the 2nd element only because it starts at index 1 and ends at index 2
print(all_fruits2) #should print ["Blueberries"]

even_fruits = fruits[::2] #will print every 2 elements in the array or even starting at 0
print(even_fruits)

odd_fruits = fruits[1::2] #will print every 2 elements in the array or even starting at 1
print(odd_fruits)

reversed_fruits = fruits[::-1] #will print the list in reverse order
print(reversed_fruits)

#since lists are mutable we can modify them

fruits = ['Apples', 'Blueberries', 'Oranges', 'Mangoes','Lemon']

fruits[0] = 'Avocado' #modify the first element
print(fruits[0]) #should print Avocado


fruits[1:3] = ['Bananas', 'Cherries'] #modify elements from index 1 to 3
print(fruits[1:3])

#adding items to a list 


#checking if an item exists in a list
does_exist = 'Apples' in fruits
print(does_exist) #should print false because of the modification above

does_exist1 = 'Lemon' in fruits
print(does_exist1)

#adding items to a list
#using append()

#fruits.append(fruit_item) #always will add at the end of the list

fruits.append('Kiwi')
print(fruits)

fruits.append('Lebron')
print(fruits)


#we can insert an item into a specific index in the array, using array_name.insert(index ,item)

fruits.insert(1, 'Curry')
print(fruits)

#remove item from a list at a specific index, using array_name.remove(item) 
# #or remove at the end array_name.pop(index)

fruits.remove('Curry')
print(fruits)

fruits.pop(1)
print(fruits)

#removing specific items or can just use pop
# syntax
lst = ['item1', 'item2','item3']
del lst[1] # only a single item
print(lst)
del lst[0:1]   # to delete the list completely

fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
#del fruits[0]
#print(fruits)       # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
#del fruits[1]
#print(fruits)       # ['orange', 'lemon', 'kiwi', 'lime']
#del fruits[1:3]     # this deletes items between given indexes, so it does not delete the item with index 3!
print(fruits)       # ['orange', 'lime']
#del fruits
#print(fruits)       # This should give: NameError: name 'fruits' is not defined


#clearing list
arr = ['item1', 'item2']
arr.clear()
print(arr)


#copying a list
arr1 = fruits.copy()
print(arr1)


#joining lists together

east_players = ['Lebron, Maxey, Embiid, Brown']
west_players = ['Curry, Wemby, Shai, Booker']

nba_players = east_players + west_players
print(nba_players )

#or use the extend method which can place the items of 1 list and the back of another
#list1.extend(list2 this list will append at the back of list1)
west_players.extend(east_players)
print(west_players) #should place the east_players behind the west

num1 = [0, 1, 2, 3]
num2= [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1) # Numbers: [0, 1, 2, 3, 4, 5, 6]
negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers) # Integers: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits ) # Fruits and vegetables: ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']


#counting items in a list, returns the number of times an item appears in the list. 
print(fruits.count('banana'))

ages = [22, 24, 19, 50, 21, 25, 21, 21, 21]
print(ages.count(21))

#finding index of an item
#array_name.index(item)
print(ages.index(50))

#reversing a list
ages.reverse()
print(ages)

#sorting a list
ages.sort() #ascending order
print(ages)

#can also use sorted() function to sort a list
sorted_ages = sorted(ages)
print(sorted_ages)

ages.sort(reverse=True)
print(ages) #sort in descending order

