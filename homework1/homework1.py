# File: homework.py

# --- Variables and Data Types ---

a = 10
print(a)
print(type(a)) # a is an interger, a whole number with no decimals

b = 1.5
print(b)
print(type(b)) # b is an float, a number which can hold decimal values

c = 3j

print(c)
print(type(c)) # c is a complex number, a number with a real and imaginary part, denoted j

d = "hello"
print(d)
print(type(d)) # d is a string, a sequence of characters defined using quotes ""

e = [1, 2, 3]
print(e)
print(type(e)) # e is a list, a collection of items which can be of different data types, defined using square brackets []

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dictionary, a collection of key-value pairs, defined using curly braces {}

g = (1, 2)
print(g)
print(type(g)) # g is a tuple, a collection of items which can be of different data types, unlike a list, tuples are immodifiable, defined using parentheses ()

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is a list, a collection of items which can be of different data types, defined using square brackets []

i = True
print(i)
print(type(i)) # i is a boolean, a data type which can only have two values

j = None
print(j)
print(type(j)) # j is a NoneType, a data type which represents the absence of

k = [True, "blue", 12]
print(k)
print(type(k)) # k is a list, a collection of items 

l = str(14)
print(l)
print(type(l)) # l is a string, a sequence of characters defined using quotes the str() operator

m = 1e4
print(m)
print(type(m)) # m is an exponential float, a number which can hold decimal values

"""
Questions:
1. How many different data types did you find?
    9
2. List all the data types you found.
    - Integer
    - Float
    - Complex
    - String
    - List
    - Dictionary
    - Set       
    - Tuple
    - Boolean
    - NoneType
3. What variables have the same data types?
    - b and m are both floats
    - e, h, and k are all lists
    - d and l are both strings
4. What was the data type of l? Why is it not an integer? What does str() do?
     The data type of l is a string, because the str() operator takes objects and returns string representations of them.
5. Look up one more data type not given above. Repeat the same procedure
"""

n = {1, 2, 3, 4, 5} 
print(n)
print(type(n)) # n is a set, a collection of unique items which can be of different data types, defined using curly braces {}


# --- Booleans ---

print(10>9) # True, 10 is greater than 9
print(10==9) # False, 10 is not equal to 9
print(10<=9) # False, 10 is not less than or equal to 9

print(bool("abc") ) # True, non-empty strings, numbers, and lists are considered True
print(bool(123)) # True, non-empty strings, numbers, and lists are considered True
print(bool(["apple", "banana", "cherry"])) # True, non-empty strings, numbers, and lists are considered True
print(bool(True)) # True
print(bool(False)) # False
print(bool(0)) # False, the number 0 is considered False
print(bool("")) # False, empty strings are considered False
print(bool(" ")) # True, a space is considered a non-empty string, and therefore True
print(bool(())) # False, empty tuples are considered False
print(bool([])) # False, empty lists are considered False
print(bool({})) # False, empty dictionaries are considered False
print(bool(True and False)) # False
print(bool(True and True)) # True
print(bool(False and False)) # False
print(bool(True or False)) # True
print(bool(True or True)) # True
print(bool(False or False)) # False
print(bool(not (False))) # True, since not false
print(bool(not (True))) # False, since not true


"""
• What pattern do you notice about expressions returning True or False?

• Which expression surprised you about its result?
• Create an expression, not given above, that will return True. Why is it True?
• Create an expression, not given above, that will return False. Why is it False?
"""

print(5==3+2) # True, 5 is equal to 3 + 2
print(5>2 and 5>6) # False, 5 is greater than 2 but not greater than 6 


# --- Arithmetic Operators ---
print(10+5) # 15, + performs addition 
print(10-5) # 5, - performs subtraction
print(2*4) # 8, * performs multiplication
print(6/3) # 2.0, / performs division, and prints a float
print(15//2) # 7, // performs floor division, and prints an integer
print(5%2) # 1, % performs modulus, and prints the remainder of the division
print(3 ** 2) # 9, ** performs exponentiation, and prints the result of raising the first number to the power of the second number

# --- Comparison Operators ---
print(5==2) # False, == checks if the two values are equal
print(10 != 10) # False, != checks if the two values are NOT equal
print(2<5) # True, < checks if the first value is less than the second value
print(12>5) # True, > checks if the first value is greater than the second value
print(5<=6) # True, <= checks if the first value is less than or equal to the second value
print(1>=10) # False, >= checks if the first value is greater than or equal to the second value

# --- Assignment Operators ---
x = 5
x += 5
print(x) # 10, += adds the value on the right to the variable on the left and assigns the result to the variable
x -= 6
print(x) # 4, -= subtracts the value on the right from the variable on the left and assigns the result to the variable
x *= 2
print(x) # 8, *= multiplies the variable on the left by the value on the right and assigns the result to the variable

# --- Logical Operators ---
"""
1. What does the operator and do? Write an expression that results in True. Write an expression
that results in False.
    The and operator returns True if both expressions are True, and False if either expression is False.    
2. What does the operator or do? Write an expression that results in True. Write an expression
that results in False.
    The or operator returns True if at least one of the expressions is True, and False if both expressions are False.
3. What does the operator not do? Write an expression that results in True. Write an expression
that results in False.
    The not operator returns the opposite of the boolean value of the expression.
"""

print(5>2 and 5>1) # True, both expressions are True
print(5>2 and 5<1) # False, one expression is False
print(5>2 or 5<1) # True, at least one expression is True
print(5>2 or 5<1) # Trywe, at least one expression is True
print(not True) # False, the opposite of True
print(not False) # True, the opposite of False

"""
1. What is the difference between / and //?
    / performs division and returns a float, while // performs floor division and returns an integer.
2. What is the difference between % and //?
    % returns the remainder of the division, while // returns the quotient of the division.
3. What operator would you use to calculate the remainder when dividing two numbers? Give
an example.
    The % operator is used to calculate the remainder when dividing two numbers. For example, 5 % 2 returns 1, which is the remainder of 5 divided by 2.
4. How do assignment operators work?
    Assignment operators are used to assign values to variables. They can also be used to perform operations on the variable and assign the result back to the variable. 
    For example, x += 5 adds 5 to the value of x and assigns the result back to x.
"""

# --- Strings ---

my_string = "hello"
print(my_string) # prints the string "hello"
print(my_string[0]) # prints the first character of the string, "h"
print(my_string[1]) # prints the second character of the string, "e"
print(my_string[2]) # prints the third character of the string, "l"
print(my_string[3]) # prints the fourth character of the string, "l"
print(my_string[4]) # prints the fifth character of the string, "o"
print(my_string[-1]) # prints the LAST character of the string, "o"
print(my_string[1:3]) # prints the second and third characters of the string, "el"
print(my_string[0:5:2]) # prints every second character of the string, "hlo"
print(len(my_string)) # prints the length of the string, 5
print(my_string + " goodbye") # concatenates the string "hello" with the string "goodbye", resulting in "hello goodbye"
print(my_string * 7) # repeats the string "hello" seven times, resulting in "hellohellohello"

"""
1. Define the term slicing. For which of the manipulations did you slice your string?
    Slicing allows you to extract a portion of a string by specifying a start and end index. 
    I sliced my string in lines 187-194
2. Call the following, describe the result:
"""
name = "Oski"
print("Hello, my name is", name)

"""
The result is "Hello, my name is Oski". The print statement concatenates the string "Hello, my name is" with the value of the variable name, which is "Oski".

3. Call the following, describe the result.
"""
name = "Oski"
print(f"Hello, my name is {name}")
"""
The result is "Hello, my name is Oski". 
4. What is the difference between the two last print statements?
Hint: Look up f-strings.
    The first print statement uses string concatenation to combine the string "Hello, my name is" with the value of the variable name.
    The second print statement uses an f-string, which allows you to embed expressions inside string literals, using curly braces {}. 
    The f-string automatically evaluates the expression inside the braces and inserts the result into the string.
"""


# --- Terminal Commands ---
# 1. cd - changes directories, use to move from one directory to another
#       Ex: cd Desktop
# 2. ls - lists the files and directories in the current directory
#       Ex: ls
# 3. ls -a - lists ALL files and directories in the current directory, including hidden files
#       Ex: ls -a
# 4. mkdir - creates a new directory inside current directory
#       Ex: mkdir new_directory
# 5 cat - prints the contents of a file to the terminal
#       Ex: cat filename.txt
# 6. pwd - prints the current working directory
#       Ex: pwd
# 7. cd .. - moves up one directory level ".." represents the parent directory
#       Ex: cd ..
# 8. cd . - stays in the current directory "." represents the current directory
#      Ex: cd .
# 9. cd ~ - moves to the home directory "~" represents the home directory
#      Ex: cd ~
# 10. cp - copies a file or directory to a new location
#      Ex: cp filename.txt new_directory/filename2.txt 
#      this command copies the file filename.txt to the directory new_directory and renames it to filename2.txt
# 11. mv - moves a file or directory to a new location, or renames a file or directory
#      Ex: mv filename.txt new_directory/filename2.txt  
#   this command moves the file filename.txt to the directory new_directory and renames it to filename2.txt
#       Ex: mv finename.txt new_filename.txt
#     this command renames the file filename.txt to new_filename.txt
# 12. rm - PERMANENTLY removes a file or directory
#      Ex: rm filename.txt
# 13. clear - clears the terminal screen
#     Ex: clear
# 14. grep - searches for a specific string in a file or files
#     Ex: grep "search_string" filename.txt
# 3 EXTRA
# 
# 15. echo - prints a string to the terminal, like print() in python
#    Ex: echo "Hello, World!"
# 16. touch - creates a new empty file
#    Ex: touch new_file.txt
# 17. rmdir - removes an empty directory
#    Ex: rmdir empty_directory

"""
2. What is the difference between ls and ls -a?
    ls lists the files and directories in the current directory, while ls -a lists all files and directories, including hidden ones.
3. What is a hidden file?
    A hidden file is a file that is not displayed when using the ls command without any flags. 
    These files typically have names that start with a period (.) on Unix-like systems.
4. Look up 3 other flags (e.g., -a was a flag for the ls command). Define and explain how to
use them on the command line.
        - -l: lists files and directories in long format, which includes additional information such as permissions, owner, group, size, and modification date.
        - -h: when used with the -l flag, displays file sizes in a human-readable format (e.g., KB, MB, GB).
        - -t: sorts files and directories by modification time, with the most recently modified files listed first.
"""