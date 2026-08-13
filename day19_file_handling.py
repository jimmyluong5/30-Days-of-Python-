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
f = open('readingexample.txt')
print(f.read()) #reads the entire file
f.close() #closes the file

