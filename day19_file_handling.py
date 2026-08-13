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

    



