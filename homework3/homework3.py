def say_goodbye(name): #prints Goodye, "name"
	print("Goodbye, ", name)



def area_circle(r): #calculates area of circle based on radius, r
	print("The area of the circle is", 3.14*(r**2))



def subtract(a, b): #subracts a from b
	return b - a

def multiply(a, b): #multiplies a times b
	return a * b

def divide (a, b): # divides a by b
	return a/b

def high_and_low_temp(readings): #returns min and max temp of the day as a tuple (min, max)
	readings = [15, 14, 17, 20, 23, 28, 20]
	return (min(readings), max(readings))

def is_weekend(day): #reads integer input and returns true if number respresents a day of the weekend
	if day <= 0 or day > 7 or day.type != int:
		return "invalid input"
	elif day != 6 or day != 7:
		return "not the weekend :("
	else:
		return "it is the weekend!!!"

def fuel_efficiency(distance, fuel): #calculates miles/gallon based on distance travelled (in miles) and fuel consumed (in gallons)
	return distance/fuel + " miles per gallon"



def encrypt(number): #removes last digits and places it in the front. the last diigit is the modulus of the number divided by 10, and the remainder is the number floor divided by 10. we need a multiplier which is whatever power of 10 we need to place the last digit in front
	last_digit = number % 10
	remaining = number // 10

	multiplier = 1
	while multiplier <= remaining:
		multiplier *= 10

	return last_digit * multiplier + remaining

def power(x, y): #raises x to th power of y
	result = 1
	for i in range(y):
		result *= x
	return result


def find_min_for(list): #returns the minimum value in a list using a for loop

	minimum = list[0]
	for number in list:
		if number < minimum:
			minimum = number
	return minimum

def find_max_for(list): #returns the maximum value in a list using a for loop

	maximum = list[0]
	for number in list:
		if number > maximum:
			maximum = number
	return maximum

def find_min_while(list): #returns the minimum value in a list using a while loop

	minimum = list[0]
	i = 0
	while i < len(list):
		if list[i] < minimum:
			minimum = list[i]
		i += 1
	return minimum

def find_max_while(list): #returns the maximum value in a list using a while loop

	maximum = list[0]
	i = 0
	while i < len(list):
		if list[i] > maximum:
			maximum = list[i]
		i += 1
	return maximum


def sum_of_digits(number): #returns the sum of the digits of a number
	sum = 0
	while number > 0:
		sum += number % 10 #adds last digit to sum
		number //= 10 #removes last digit from number by dividing it by 10 using floor division
	return sum

number = 2066939314
sum = sum_of_digits(number)
print("The result of sum of the digits (6.3) of", number, "is", sum)
