#dictionaries

#collection of unordered, modifiable, indexed (but not by index number, but by keys) 
#hashset or hashtable #match the correct key and access the data you want O(1) constant time operation
#creating a dictionary using {} or dict()

#empty dictionary dict_name = {}

dict_name = {} #empty dictionary

dict = {'key1', 'key2', 'key3', 'key4', 'key5'}

#dictionaries can store different data types
#strings, sets, lists, tuples, booleans and other dictionaries (nested dictionaries)
jimmy = {'Age':'17', 'hobbies': {'gaming', 'volleyball'} }  #you can see how 'hobbies' is now a value of a key named 'hobbies' and 'gaming' is its value

#key and its key value (item and its value)
dct = {'key1' : '2', 'key3': ['a', 'b', 'c']} #key1's value is 2, to access it, you must use the key

#dictionary length
print(len(dct)) #determines the number of key : value pairs in the dictionary.set

#we can access the dictionary using keys (not index numbers, it's not indexed by numbers 
print(dct['key1']) #2 

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(person['first_name']) # Asabeneh
print(person['country'])    # Finland
print(person['skills'])     # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0])  # JavaScript
print(person['address']['street']) # Space street
#print(person['city'])       # Error

#if the key doesn't exist, we can use the .get() method to return a default value
print(person.get('city')) # None

#adding items to a dictionary (normal way)
dct['key2'] = 'key2_value'
print(dct)

#or you can use append or extend 
dct['key3'].append('key3_value') #append only works if the key is an array/list
print(dct)


#we can modify items in a dictionary
dct['key1'] = 'lebron'
print(dct)

#checking keys in a dictionary
print('key1' in dct) #True
print('key1' not in dct) #False

#removing key and value pairs from dictionary
#using pop(key) - removes item with the specified key name
#using popitem() - removes the last item added
#using del - removes the item with the specified key name or removes the dictionary itself
#using clear() - removes all items from the dictionary

dct.pop('key1')
print(dct)
dct.popitem()
print(dct)

dct.pop('key3')
print(dct)

#converting dictionary into list of items, keys, and values
#the items() method changes the dictionary to a list of tuples
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])


#copying a dictionary
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy()
print(dct_copy)

#getting dictionary keys as a list
keys = dct.keys()
print(keys)

#getting dictionary values as a list
values = dct.values()
print(values)

#exercises

dog = {} #empty dictionary
dog = {'Name': 'Doggo', 'breed': 'Golden Retriever', 'legs': 4, 'age': 2}

student_dict = {'first_name': 'Jimmy', 'last_name':'Luong', 'Gender': 'Male', 'age': 20,}

print(len(student_dict))

values_student_dict = student_dict.values()
print(values_student_dict)

keys_student_dict = student_dict.keys()
print(keys_student_dict)

keys=list(keys_student_dict)
print(keys)

values=list(values_student_dict)
print(values)

#change dictionary into list of tuples using item()

print(student_dict.items())

student_dict.popitem()
print(student_dict)

del student_dict
#print(student_dict) #error

