#package manager
#Python PIP python package manager 
#PIP - stands for Preferred Installer Program

#to upgrade pip

#pip install --upgrade pip
#we use pip to install different Python modules 
#Package is a Python module that can contain one or more modules or other packages

#a moduleor modules that we can install to our application is a package. In programming,
#we dont have to code everything we can just install packages and import them to our applications.PythonFinalizationError

# install numpy by doing 
#pip install numpy - Numpy stands for numeric python 
""" NumPy is the fundamental package for scientific computing with Python. It contains among other things:
a powerful N-dimensional array object
sophisticated (broadcasting) functions
tools for integrating C/C++ and Fortran code
useful linear algebra, Fourier transform, and random number capabilities """

#pandas is an open source open source library providing high performance
#easy to use data structures and data analysis tools for the python programming language.



#we can import web browser modules too, which can help us open any website. we don't need to install 
#this module, its built in

#if you want to open any websites this module can be used
import webbrowser

""" url_lists = [
    "www.google.com",
    "www.youtube.com",
    "www.facebook.com",
    "www.twitter.com",
    "www.instagram.com",
    "www.linkedin.com",
    "www.github.com",
    "www.reddit.com",
    "www.stackoverflow.com",
    "www.python.org",    
]
#opens the list of websites above
for url in url_lists:
    webbrowser.open(url) """

#type pip list in the terminal to see what pip has installed

#pip show package to show the packages information  
#eg pip show numpy

#reading from url 
#we would like to read from a website using url or from an API 
#API - stands for Application Program Interface,
#it is a means to exchange structured data between servers primarily as json data.
#to open a network connection, we need a package called requests - it allows to open a
#network connection and to implement CRUD (create, read, update and delete operations)

#we can install requests using pip install request
#we will see get, status_code, headers, text and json methods in requests module:

#get() - to open a network and fetch data from url - it returns a response object.
#status_code - after we fetch data, we can check the status of the operation (success, failure)
    #for status_code success = 200-299
    #100-199 - the server is working on the request 
    #200-299 - the server got the request and it was understood and accepted
    #300-399 - client must take extra steps to finish the request, like going to a new web address
    #400-499 - client error, the request has bad syntax or cannot be filled because of a client issue


    #500-599 - server error - the server failed to complete the request 
    #headers - contains meta information about the request and response. It's a key-value pair collection.
    #we can use headers to check things like content type, content length, etc.content-type is a 
    #header that specifies the media type of the resource, e.g. application/json or text/html
    #text - returns the response body as a string.
    #json - returns the response body as a Python dictionary (if the response is valid JSON). 


    