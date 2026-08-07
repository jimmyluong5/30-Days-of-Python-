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



