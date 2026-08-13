#file handling

#we can store data in different file formats, such as .txt, .json, .xml, .csv, .tsv , .excel

#file handling allows us to modify, read, update and delete files
# to handle data we use open()

#syntax
""" open('filename', mode) modes(r, a, w, x, t, b)
r = read - opens a file for reading, returns error if the file doesn't exist
a = append - opens a file for appending/adding, creates the file if it doesn't exist
w = write - opens a file for writing, creates a file if it doesn't exist.
x = create - creates the specified file, returns an error if the file exists
t = text - default value, used for text files
b = binary - used for binary files like images, audio, video, etc
"""

#opening files for reading

#default mode of open() is reading so we don't need to specify a mode.
f = open('readingexample.txt') #must be in the same folder as the 30 days of python folder.
print(f.read()) #reads the entire file
f.close() #closes the file

#f.read() reads the file
#f.close() closes the file

#instead of printing all the text lets just print the first 5
f = open('readingexample.txt')
print(f.read(6))
f.close()


#we can read only the first line
#using readline()

f = open('readingexample.txt')
first_line = f.readline()
print(first_line)
f.close()


#we can read all the lines using readlines()
#this returns a list of lines
f = open('readingexample.txt')
lines = f.readlines()
print(lines)
f.close() 
#the lines of text are separated by \n

#another way to get all the lines as a list is using splitlines()
f = open('readingexample.txt')
lines = f.read().splitlines()
print(lines)
f.close()

#after we open a file we should close it. there is a new way to open files using (with)
#which closes the file by its self
with open('readingexample.txt') as f:
    lines = f.read().splitlines()
    print(lines)



#now we can open files for writing and updating

#to write to an existing file we must add a mode as a parameter to the open function as w - write, 

with open('readingexample.txt', 'a') as f:
    f.write('This text will be appended to the end') #don't forget the mode

with open('newfile.txt', 'w') as f: #this creates a new text file in the folder of 30 days of Python.
    f.write('Lebron James and the 76ers')
    f.write('Steph Curry and the Golden State Warriors')

#deleting files
import os
if os.path.exists('gabby_is_a_fn.txt'):
    os.remove('gabby_is_a_fn.txt')
    print('file removed')
else:
    print('file does not exist')
    

#file types now

#.txt is common, but we should deal with .json now

#.json stands for JavaScript Object Notation
#it is used to store and transport data. it is human readable
#it is a stringified JavaScript object or Python directionary

dict = {'Lebron', 'Curry', 'Giannis', 'Lillard'}

#dictionary to string
person_dict= "{'Lebron', 'Curry', 'Giannis', 'Lillard'}"
print(person_dict)

#changing JSON to dictionary

#we import the json module

import json #then we use the loads method to convert a string to a dictionary

person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScript", "React", "Python"]
}'''

person_dict = json.loads(person_json)

print(person_dict)
print(person_dict['name'])

import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScript", "React", "Python"]
}
# let's convert it to  json
person_json = json.dumps(person, indent=4) # indent could be 2, 4, 8. It beautifies the json
print(type(person_json))
print(person_json)

#we can save our data as a json file

with open('json_example.json', 'w') as f:
    json.dump(person, f, ensure_ascii = False, indent = 4)


#to normally write a json file
with open('example.json', 'w') as f:
    json.dump(person, f, ensure_ascii = False, indent = 4) 

#can remove example.json by doing os.remove('example.json')

#person is the python object, so if i used something else it would be
#name_json and it would be name instead of person

#f is the open, writable file object created by with open('blahblah.json') as f:
#json.dump() writes directly to the file

#ensure ascii == False is to allow us to write non ascii characters, such as emojis or accents
#indent = 4 just indents the text by 4 spaces of indentation.__debug__



#files with csv extension
import csv

#to create a .csv file
with open('test.csv', 'w') as f:
    csv_writer = csv.writer(f, delimiter=',')
    csv_writer.writerow(['name', 'city', 'weight'])
    csv_writer.writerow(['jimmy', 'nyc', 175])

#to read a .csv file
with open('test.csv', 'r') as f:
    csv_reader = csv.reader(f, delimiter=',')
    for row in csv_reader:
        print(row)


#files with xlsx extension


import openpyxl #its an l.

#create a workbook and select active sheet
workbook = openpyxl.Workbook()
worksheet = workbook.active
worksheet.title = "SampleSheet"

#add data
worksheet.append(['Name', 'age'])
worksheet.append(['Jimmy', 20])
worksheet.append(['Lebron', 42])

workbook.save('sample.xlsx')

#files with xml extension

import xml.etree.ElementTree as ET 

#to create an .xml file using Python code:
root = ET.Element('person', attrib={'gender': 'female'})
name = ET.SubElement(root, 'name')
name.text = 'Asabeneh'
country = ET.SubElement(root, 'country')
country.text = 'Finland'
city = ET.SubElement(root, 'city')
city.text = 'Helsinki'
skills = ET.SubElement(root, 'skills')
skill1 = ET.SubElement(skills, 'skill')
skill1.text = 'JavaScript'
skill2 = ET.SubElement(skills, 'skill')
skill2.text = 'React'
skill3 = ET.SubElement(skills, 'skill')
skill3.text = 'Python'

tree = ET.ElementTree(root)
tree.write('xml.example.xml', encoding='utf-8', xml_declaration=True)

#to read/parse an .xml file:
tree = ET.parse('xml.example.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field: ', child.tag)


    