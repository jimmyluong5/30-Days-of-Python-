#list comprehension is a way to create a list from a sequence, basically its a short way to create a list
#list comprehension is considerably faster than using the for loop

#syntax 
#[expression] for i in iterable if condition]

#for instance if you want to change a string to a list of characters . you can use a couple methods

language = 'Python'
lst=list(language)
print(lst)

#another way
lst = [i for i in language]
print(lst)

numbers = [i for i in range(11)] #produces a list of numbers from 0 to 10
print(numbers)

squares_numbers = [i*i for i in range(11)] #produces a list of squared numbers
print(squares_numbers)

# It is also possible to make a list of tuples
numbers = [(i, i * i) for i in range(11)]
print(numbers) ## [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

#list comprehension can be combined with if expressions
even_numbers = [i for i in range(11) if i % 2 ==0]
print(even_numbers)

odd_numbers = [i for i in range(11) if i % 2 !=0]
print(odd_numbers)

#filtering numbers
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in range(11) if [i>0, i%2==0]]
print(positive_even_numbers)
