# name = "Lemoni"

# # print("Hello,", name)

# # def say_hello(name):   # funcrtion with print statement
#   #  print("Hello,", name)

# # say_hello(name)

# def add(a, b):  
#     print(a + b)

# add (7, 8)

# """
# OR, BETTER PRACTICE:

# def add(a, b):
#     return a + b

# print(add(7, 8))

# """

# # --- CONDITIONAL STATEMENTS ---
# # if - MAIN CONDITION checkes if a condition is true, and executes a block of code if it is true
# # elif - SECONDARY CONDITION checks if a condition is true, and executes a block of code if it is true, if not it checks the next condition
# # else - executes a block of code if none of the previous conditions are true
# """
# if x%2==0:
#     print("x is even")
# else:
#     print("x is odd")


# def check_num(num):
#     if num > 0:
#         return "positive"
#     elif num < 0:
#         return "negative"
#     else:
#         return "zero"

# print(check_num(32))

# # and - both conditons must be true
# # or - only one condition must be true

# print(True and True) #prints true
# print(True and False) # prnts false
# print(True or False) # prints true
# print(False or False) #prints false

# """

# """
# def can_vote(age, is_citizen):
#     if age >= 18 and is_citizen:
#         print("You can vote!")
#     else:
#         print("You can't vote!")

# can_vote(21, True)
# """
# """
# def is_weekend(day):
#     if day=="Saturday" or day == "Sunday":
#         return "It's the weekend"
#     else:
#         return "It is not the weekend :("

# print(is_weekend("Monday"))
# # """
# # # --- LOOPS ---
# """
# WHILE LOOP
# i = 10
# while i>0:
#     i -= 1
#     print i

# """

# # for loop eg.:

# #for i in range(10):
#  #   print(i)

# fruit_basket = ["Lyhee", "mango", "nectarnes"]
# for fruit in fruit_basket:
#     print(fruit)

# while loop eg.:

# def countdown(start):
#     while start > 0:
#         print("T-",start)
#         start -= 1
#     print("Lift off")

# # countdown(10)

# list = [40, 80, 10, 30, 50, 20]

# def minimum(list):
#     return min(list)
# print(minimum(list))

# # def(min(list)):

# create a function to determine if a positive integer is a prime number
# def isprime(num):
#     if num <= 0 and type(num) != int:
#         return "try again, choose a new number"
#     else :
#         if num == 1:
#             return "neither"
#         elif num == 2:
#             return "is prime"
#         else:
#             if num % 2 == 0:
#                 return "not prime"
#             else:
#                 for i in range (1, num):
#                     if num % i == 0:
#                         return "not prime"
#                     else: 
#                         return "prime number"


# --- 9/28 LECTURE ---
# lists are ordered arrays, values are contained in brackets [ ] and seperated by commas. Order of list is maintained
# 1) .append( ): Adds an element to the end of the list.
# 2) .extend( ): Appends the elements of another list to the end of the current list.
# 3) .insert( ): Inserts an element at a specified position in the list.
# 4) .remove( ): Removes the first occurrence of a specified value from the list.
# 5) .pop( ): Removes and returns the element at the specified index (default is the last
# element).
# 6) .clear( ): Removes all elements from the list.
# 7) .index( ): Returns the index of the first occurrence of a specified value.
# 8) .count( ): Returns the number of occurrences of a specified value in the list.
# 9) .sort( ): Sorts the elements of the list in ascending order
# 10) .reverse( ): Reverses the order of the elements in the list.
# 11) .copy( ): Returns a shallow copy of the list


# numbers = [1, 2, 3, 4, 5]
# 
# print(numbers[0]) #prints number in first position of the list
# print(numbers(-1)) #prints last element
# print(numbers[-2]) #prints second to last element of list
# numbers.append(6) 
# print(numbers)
# fruits = ["apple", "cherries", "bananas"]

# fruits[0] = "grapes" # replaces first item in fruits with grapes.
# print(fruits)

# numbers.pop(0) #removes item in first place

# # --- ADVANCED LIST TECHNIQUES
# # Slicing - grabbing a potion of the list list[a:b] starts at a -1 and ends at b-1

# print(numbers[1:3])


# Striding - grabbing a portion of a list with a step pattern     list[::2] - every second item in list starting at index 0
#                                                                   list[a:b:c] - [start:stop:step]

# num =[10, 20, 30, 40, 50, 60]
# print(num[1:4]) 

# print(num[1:5:2])


# --- DICTIONARIES ---
# use curly brackets { } each key valued pair is seperated by commas

# bugs ={
#     "ants":["black", "fire"],
#     "spiders":["black widow", "tarantula"],
#     "flys":["horse", "house"]
# }

# print(bugs.values())
# print(bugs.keys())
# print(bugs.items())

# del bugs["ants"]
# print(bugs)

# list1 = list(range(0,11))
# print(list1)
# print(list1[0:5])
# print(list1[::2])
# print(list1[-1::-1])


a = [2, 4, 6]
b = [8, 10, 12]
c = [14, 16, 18]

nested_list = [a, b, c]

print(nested_list[2][1])