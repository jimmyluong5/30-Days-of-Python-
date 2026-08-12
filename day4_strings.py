#day4 - strings


#creating a string could be done in many ways such as 
string_name = 'string here'

#or by printing strings or letters
print('This is a string')
#strings can also be created using double quotes or single quotes, it doesn't matter

#you can also create multi-line strings using triple quotes
multi_line_string = '''This is my string'''
print(multi_line_string) #you can also do the same with double quotes


#string concatenation (literally just add the strings together)
firstname='Jimmy'
lastname='Luong'
space=' '
fullname = firstname+space+lastname
print(fullname)


#\n: new line
#\t: Tab means(8 spaces)
#\\: Back slash
#\': Single quote (')
#\": Double quote (")
#but in python when you print anyways it comes with a new line character


#formatted strings (old way)
firstname='Jimmy'
lastname='Luong'
fullname ='My name is %s %s' %(firstname, lastname)
print(fullname)


#formatted strings (new way)
firstname='Jimmy'
lastname='Luong'
formatted_string = 'I am {} {}'.format(firstname, lastname)
print(formatted_string)

a = 4
b = 3

print('{} + {} = {}'. format(a, b, a+b))

#printing strings by indices
string = 'Lebron'
print(string[0])
print(string[1])

#slicing strings
string = 'Lebron'
print(string[0:3]) #this prints the first 3 letters from index 0 to index 2
#excluding 3
print(string[2:]) #this prints from index 2 to the end
print(string[:4]) #this prints from the start to index 3

#reversing a string
print(string[: :-1])#prints the string backwards, the colon (:)
#means the whole string and the -1 means step backwards by 1 starting
#from the end of the string

#using string commands in the python library
#find() this finds an occurence of a substring in another string and returns the index
#else it returns -1

string = 'Hello world'
print(string.find('o')) #this returns 4, the first index where 'o' is found

print(string.find('z')) #this returns -1 since 'z' is not found in the string

#upper() this converts a string to uppercase
lebron = 'hello'
print(lebron.upper())

#lower() this converts a string to lowercase
string = 'HELLO'   
print(string.lower())

#strip() this removes any whitespace from the beginning or end of a string
string = '   hello world   '
print(string.strip())

#replace() this replaces a substring with another substring
string = 'hello world'
print(string.replace('world', 'there'))

#to find the if the string is all lower case or uppercase
string = 'hello'
print(string.islower()) #returns True, else it returns false

#can also use a list/array of strings and join them together.
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'


#exercises
#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

string1 = ['Thirty', 'Days', 'Of', 'Python']
string2= ' '.join(string1)
print(string2)

#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
string1 = ['Coding', 'For', "All"]


#need to remove all the spaces first 
str1 = 'Lebron James'
string2 = str1.replace(' ','')
print(string2)

#to check if the string has non-alphanumerical characters
str1 = 'Lebron James!!!'
if str1.isalnum() == True:
    print('String has no non-alphanumerical characters')


#this method strips all spaces, and non-alpha characters
str1 = 'Lebron@@!#_James !!! Curry'
str1 = ''.join(i for i in str1 if i.isalnum())
print(str1)

#convert a string to ascii
str1 = "{}"
str1 = [ord(char)for char in str1]
print(str1)


# check if the abs() between the left and right ptrs are within the values of 1 and 2.str1

