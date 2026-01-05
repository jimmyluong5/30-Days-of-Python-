#day4 - strings


#creating a string could be done in many ways such as 
string_name = 'string here'

#or by printing strings or letters
print('This is a string')
#strings can also be created using double quotes or single quotes, it doesn't matter

#you can also create multi-line strings using triple quotes
multi_line_string = '''This is my string'''
print(multi_line_string) #you can also do the same with double quotes


#string concatenation 
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

