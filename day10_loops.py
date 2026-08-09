#loops

#while loops, while a condition is going on do the following code
i = 0
#while i < 10:
   # print(i)
   # i= i+1

#break and continue
#use break when we would like to get out of a loop

while i < 10:
    print(i)
    i=i+1
    if i == 5:
        break

#here i = 5 right now
print("random string")
#with continue we can skip the current iteration at that condition like i==5
#while i < 10:
  #  print(i)
 #   i=i+1
  #  if i==6:
   #     print("lebron")
    #    continue #skips the next line of code and jumps back to the start (while i<10)
    #   i=i+1 #line won't execute

   



#for loop
#syntax: for iterator in sequence: 
    #do something


#example
for i in range(5): #this means i stops at the fifth index, from 0 - 4
    print('*' * i) #prints a triangle stops at 4 stars.

print('\n')

numbers = [0, 1, 2, 3, 4, 5]
for i in range(len(numbers)):
    print(i)





