fav_foods = ["pizza", "soup dumplings", "yogurt", "burrito bowl", "watermelon"]
"""
I had an error becuase i forgot to include a comma between "burrito bowl" and "watermelon" in the list.
"""
print(fav_foods[1]) #prints soup dumplings  
print(fav_foods[-1]) #prints watermelon 
fav_foods.append("ice cream") #adds ice cream to the end of the list
fav_foods.insert(0, "apple") #adds apple to the beginning of the list
del fav_foods[2] #deletes yogurt from the list
print(len(fav_foods)) #prints the length of the list

for food in fav_foods:
    print(food.upper())

first_and_last = [fav_foods[0], fav_foods[-1]] #creates a new list with the first and last items of fav_foods
print(first_and_last) #prints the new list

for food in fav_foods:
    if food == "potato":
        print("A potato!")
    else:
        print("No potato!")

numbers = list(range(21)) #creates a range of numbers from 0 to 20

def get_first_15(numbers):
    first_15 = numbers[:15]
    return first_15

print(get_first_15(numbers)) #prints the first 15 numbers in the range

def get_every_5th(first_15):
    every_5th = first_15[0::5]
    return every_5th

print(get_every_5th(get_first_15(numbers))) #prints every 5th number from the first 15 numbers

def reverse_and_stride(every_5th):
    reversed_and_strided = every_5th[::-3]
    return reversed_and_strided

print(reverse_and_stride(get_every_5th(get_first_15(numbers)))) #prints every 5th number from the first 15 numbers in reverse order with a stride of 3


list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = [7, 8, 9]
numbers = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

print(numbers[2])
"""
I accidentally said numbers[3] instead of numbers[2].
"""
print(numbers[1][1]) #prints the second element of the second list

numbers.append([10, 11, 12]) #adds a new list to the end of the numbers list

def sum_nested(numbers):
    total = 0
    for sublist in numbers:
        total += sum(sublist)
    return total

print(sum_nested(numbers)) #prints the sum of all numbers in the nested list

def create_5by5():
    matrix = []
    number = 1
    for row in range(5):
        new_row = []

        for col in range(5):
            new_row.append(number)
            number += 1
        matrix.append(new_row)
    return matrix

numbers = create_5by5() #creates a 5x5 matrix with numbers from 1 to 25
print(numbers) #prints the 5x5 matrix

def replace_multiples_of_3(numbers):
    for row in range(5):
        for col in range(5):
            if numbers[row][col] % 3 == 0:
                numbers[row][col] = "?"
            
    return numbers

print(replace_multiples_of_3(numbers)) #prints the 5x5 matrix after replacing multiples of 3 with "?"


def sum_non_question_marks(numbers):
    total = 0
    for row in numbers:
        for item in row:
            if item != "?":
                total += item
    return total

print(sum_non_question_marks(numbers)) #prints the sum of all numbers in the 5x5 matrix that are not "?"




ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}

print(ages["Katie"]) #prints the age of Katie

ages["Mira"] = 100
ages["Milana"] = 52
del ages["Mariam"]

for person in ages:
    print(person, ages[person])