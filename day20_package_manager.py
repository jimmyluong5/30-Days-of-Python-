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


#lets fetch some data from this website: https://www.w3.org/TR/PNG/iso_8859-1.txt
import sys
sys.stdout.reconfigure(encoding='utf-8')

import requests # importing the request module


"""  url = 'https://raw.githubusercontent.com/Asabeneh/30-Days-Of-Python/master/data/romeo_and_juliet.txt'
response = requests.get(url) # opening a network and fetching a data
print(response)
print(response.status_code) # status code, success:200
print(response.headers)     # headers information
print(response.text) # gives all the text from the page"""

#let us read from an API

""" An API, or Application Programming Interface, is a set of defined rules and 
protocols that allows different software applications to communicate and share data with each other. """


#using the requests module
import sys
import requests
sys.stdout.reconfigure(encoding='utf-8')

#1 endpoint and authorization
url = 'https://api.restcountries.com/countries/v5?q=japan'

#api key which allows us access to the api
headers = {'Authorization': 'Bearer rc_live_06829e1750294ca6b2e09b5c06872868'} 

#2 make the GET request
response = requests.get(url, headers = headers)
print("Status Code", response.status_code)

#3 Parse JSON & Extract fields

if response.status_code == 200:
    data = response.json() #so we get the data here in json format

    #extract the first country 
    country = data['data']['objects'][0]

    # Extract capital names using a standard for loop
    capitals = []
    for cap in country['capitals']:
        capitals.append(cap['name'])

    print("\n--- Country Details ---")
    print("Common Name:", country['names']['common'])
    print("Official Name:", country['names']['official'])
    print("Capitals:", ", ".join(capitals))
    print("Region:", country['region'])
    print("Population:", f"{country['population']:,}")
else:
    print("Failed to fetch data")    

#if you want, to change the country you can change q = Japan or like any other country


#simple steps with APIs

#1 Request URL (http://api.open-notify.org/iss-now.json) #the url we are using to get the data

#2 Response (Receieve) - Retrieve the data, the server returns a status code (200 which is success), 
#and a data payload in the form of a .json file. 

#3 Parse & Use (breakdown the data and use it) - convert that JSON data into
# python dictionary and extract information. You can use the data however, you want to print it,
#analyze it, display it in a UI, or save it to a database.data

#4 Main Types of API requests (CRUD)


"""GET: retrieves data from a resource.
example: would be seraching for country data, weather info, stock prices


POST: creates a new data or sends new data to a server.
example: submitting a sign up form, posting a tweet, creating a post on social media,
uploading a file


PUT: updates an existing data.
example: modifies existing data, updating profile picture or bio


DELETE: deletes a data.
example: deleting a tweet or post, would need the id of the tweet or post, API of the social media platform.


Real-World Examples of What You Can Build
Weather Dashboard: Use a weather API to fetch temperature & forecasts for any city.
Crypto Tracker: Use CoinGecko API to fetch live prices for Bitcoin, Ethereum, etc.
AI Apps: Send text to OpenAI/Gemini API and get back AI responses or generated images.
E-Commerce: Send shopping cart items to Stripe API to handle credit card payments.
"""

"""Never hard code the API keys, or upload them to github. If they are paid API keys, 
someone could take it and run up your bills. Better use environment variables 
to store the API keys. """













