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

url_lists = [
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
    webbrowser.open(url)
        