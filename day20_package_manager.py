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

#create a .gitignore file, then put .env in it
#create a .env file and put the api key in there (e.g.) (countries_api = rc_live_06829e1750294ca6b2e09b5c06872868)
#then call it here.


#to access the API key 
import os
from dotenv import load_dotenv

#load the variables from the .env file into the environment
load_dotenv()

#fetch the key using os.getenv()
api_key = os.getenv('REST_COUNTRIES_API_KEY')
#then use it in the API headers


#1 endpoint and authorization
url = 'https://api.restcountries.com/countries/v5?q=japan'

#api key which allows us access to the api
headers = {'Authorization': f'Bearer {api_key}'} 

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

""" #exercise
#Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
url = 'https://raw.githubusercontent.com/Asabeneh/30-Days-Of-Python/master/data/romeo_and_juliet.txt'
response = requests.get(url)
print(response.status_code)

if response.status_code == 200:

    text = response.text #in the form of a string
    text = text.lower()

    #to remove the puncuation, we can use the string module 
    import string

    for char in string.punctuation:
        text = text.replace(char, '')

    #we can convert long string into a list of words, using text.split() which splits the string at every whitespace

    words = text.split()
    
    #then create a hashmap to count the frequency of words
    hashmap = {}

    #then we loop through the list of words and count the frequency of words in the hashmap
    #first we loop through the entire list of words
    for word in words:

        #if the word is in the hashmap we increase the frequency by 1
        if word in hashmap:
            hashmap[word] +=1
        else:
            #we add it to the hashmap
            hashmap[word] = 1
    
    #here we have a hashmap filled with the frequency of words.

    #then we have to sort the words based on frequency using the sort function

    # to sort the words based on frequency using the sorted() function:
    # - hashmap.items() converts dict to a list of (word, count) tuples
    # - key=lambda x: x[1] sorts by the frequency count
    # - reverse=True sorts from highest frequency to lowest
    sorted_words = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
    
    print("\n--- Top 10 Most Frequent Words (Using sorted + lambda) ---")
    print(sorted_words[:10])

    # Or we can use the Counter class from the collections module
    from collections import Counter
    word_counts = Counter(words)
    print("\n--- Top 10 Most Frequent Words (Using Counter) ---")
    print(word_counts.most_common(10)) """






#exercise 2

""" Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
the min, max, mean, median, standard deviation of cats' weight in metric units.
the min, max, mean, median, standard deviation of cats' lifespan in years.
Create a frequency table of country and breed of cats """   

url = 'https://api.thecatapi.com/v1/breeds'
response =requests.get(url)

if response.status_code == 200:
    #then we get the data in the form of .json
    data = response.json()
    
    weights = []

    #in order to find what the structure looks like, we can print the first item
    #print(data[0])
    #we found out that the first index is an array of data.
    #weight is in the first column so ['weight']['metric'] to access the weight values

    #then if we want to access lifespans we can use ['life_span'] to get the lifespans.

    print(data[0]['weight']['metric']) #prints 3-5 kg
    print(data[0]['life_span']) #prints 11-15
    #or the keys of the data
    #print(data[0].keys())

    # Calculate min, max, mean, median, standard deviation of cat's weight in metric units
    import statistics
    
    weights = []

    for breed in data:
        weight_data = breed['weight']['metric']  # e.g., "3 - 5"
        weights_split = weight_data.split('-')
        
        for item in weights_split:
            weights.append(float(item))
    
    # Calculate statistics
    min_weight = min(weights)
    max_weight = max(weights)
    mean_weight = sum(weights) / len(weights)
    median_weight = statistics.median(weights)
    stdev_weight = statistics.stdev(weights)

    print("\n--- CAT WEIGHT (kg) STATS ---")
    print("Min Weight:", min_weight)
    print("Max Weight:", max_weight)
    print("Mean Weight:", f"{mean_weight:.2f}")
    print("Median Weight:", median_weight)
    print("Std Dev Weight:", f"{stdev_weight:.2f}")    