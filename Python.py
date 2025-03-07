"""\
# Write a Python program that prints your favorite sport.

print("My favorite sport is Cricket")

# Store the name of your favorite volleyball player in a variable and print it.

name = "Ab Devillers"
print(f"My favorite cricketer is {name}")

# Ask the user for their name and print a greeting.
name = input(" What is your name? ")
print(f"Hello  good morning {name}, have a nice day")

# Ask the user for two numbers and print their sum.

Num1 = int(input("Enter first number: "))
Num2 = int(input("Enter second number: "))
Sum = (Num1) + (Num2)
print(f"Sum of two numbers is {Sum}")

# Ask the user how many hours they train per day and how many days they train per week. Then, calculate their total weekly training time.

Num_hr = int(input("Enter number of hours you train per day:  "))
Num_days = int(input("Enter number of days you train per week:  "))
Total = (Num_hr)*(Num_days)
print(f"Total weekly training time is {Total}")

# Write a Python program that asks for a volleyball team's score and checks if they won, lost, or if it's an invalid score.

Teams_score  = int(input("Enter the  Team's score: "))
Opponents_score  = int(input("Enter the  Opponent's score: "))

if Teams_score > 25 or Opponents_score > 25:
    print("It is a invalid score")
elif Teams_score < 0 or Opponents_score < 0:
    print("It is a invalid score, score cannot be negative")
elif Teams_score > Opponents_score:
    print("They have won the game of volleyball")
elif Teams_score < Opponents_score:
    print("They have lost the game of volleyball")

# Write a program that prints numbers from 25 to 0 using a loop.

for i in range(25,-1,-1): # range(start, stop, step)
    print(i)

# Write a Python program that keeps asking the user "Did you serve correctly? (yes/no)"


while True:
    question = input("Did you serve right?(yes/no): ")
    if question == "no":
        print("Try again!")
    elif question == "yes":
        print("Great! You can now start the game.")
        break
    else:
        print("Enter yes or no")

# Write a Python program that takes 6 player names as input and prints the list.

players_list = [input("Enter the players name: ") for i in range(1,7)]
print(players_list)
players_dict = {index: value for index, value in enumerate (players_list)}
print("Team lineup: ", players_dict)


names = ["Alex", "Bob", "Alice", "John"]
name_A = [name for name in names if name.startswith("B")]
print(name)

#Functions
#def functio_name(parameters):
    #code
#return value #optional

def greet_player(name, age, weight):
    print(f"Hello,{name} get ready for the game, you are {age} year old and your {weight} KG weight is light")

greet_player("Pradyumna", 28, 58)

names = ["First", "Second", "Third"]
num = [int(input(f"Enter the {item} number which you like to add: "))for item in names]
print(num)

def add_number(a,b,c):
    return a+b+c
result = add_number(num[0], num[1], num[2])
print("Sum of three number is: ", result)

def player_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

player_info(Name="Pradyumna", Position="Setter", Jersey=10) 

#Ternary operator : Writing if else in single line.

# Check if a Number is Even or Odd
num = int(input("Enter the number: "))
condition = "Even" if num % 2 == 0 else "odd"
print(condition)

# Shorter Way to Find the Maximum of Two Numbers
num_1 = int(input("Enter the frist number: "))
num_2= int(input("Enter the second number: "))
condition = "First Number is MAX" if num_1 > num_2  else "Second number is bigger"
print(condition)

# Checking if a number is positive, negative, or zero.
num = int(input("Enter the number: "))
Result = "Positive" if num > 0 else "Zero" if num == 0 else "Negative" 
print(Result)

# Finding the smallest of three numbers.
names = ["First", "Second", "Third"]
numbers = [int(input(f"Enter the {item} number: ")) for item in names]
print(numbers)
condition = "All numbers are equal" if numbers[0] == numbers[1] == numbers[2] else "first number is the smallest" if numbers[0] <= numbers[1] and numbers[0] <= numbers[2] else ("Second number is the smallest" if numbers[1] <= numbers[0]  and numbers[1] <= numbers[2] else "Third number is the smallest")
print(condition)

# Write a function to calculate the factorial of a number.

def factorial(number):
    if number < 0:
        return "Factorial is not defined for negative number"
    total = 1
    for item in range(1, number +1):
        total *= item
    return total
num = int(input("Enter a number for which you would like to know the factorial: "))
result = factorial(num)
print(f"The Factorial of {num} is: {result}")

# Write a program to remove duplicates from a list.
def dupicalte_removal(num):
    number =[]
    for idx, item in enumerate(num[0:]):
        for i in num[idx+1:]:
            if item == i:
                number.append(idx)
    print(number)
    
    for item in number:
          num.remove(num[item])     
    return num
numbers = [int(input("Enter the number: ")) for item in range(5)]
result = dupicalte_removal(numbers)
print("Removed duplicates are: ", result)

number =[1,1,2,3,6]
item = set(number)
number = list(item)
print(item, number)


cities = ("Banglore", "Bonn", "Mysore", "Koln", "Heddur")
for item in cities:
    print(item)


def dupicalte_removal(num):
   number =[]
   for item in num:
      if item not in number:
         number.append(item)
   return number
numbers = [int(input("Enter the number: ")) for item in range(5)]
result = dupicalte_removal(numbers)
print("Removed duplicates are: ", result)

#Use a set to store unique words from a sentence
sentence = input("Enter the sentence: ")
words = sentence.split()
unique_words = set(words)
print(unique_words)


# Write a Python program where a user enters player names and their jersey numbers, then print the dictionary.
dictionary = {}
name = input("Enter the player name: ")
number = int(input("Enter the jersey name: "))
dictionary[name] = number 
print(dictionary)

# Write a program that swaps two variables without using a third variable.
Var_1 = "Hello"
Var_2 = "Good Morning"
print(f"before swaping {Var_1} , {Var_2}")
Var_1, Var_2 =  Var_2, Var_1
print(f"After swaping {Var_1} , {Var_2}")

# Write a program that removes duplicate numbers from a list using a set.

numbers_list = list(map(int, input("Enter the numbers separated by spaces: ").split()))
unique_numbers = set(numbers_list)
print("original_list:", numbers_list)
print("unique_numbers: ", list(unique_numbers))

#Write a Python program that takes a list of numbers from the user and prints the maximum and minimum values.

Numbers_list = list(map(int, input("Enter the number separated by space: ").split()))
print("Maximum value in the list is: ", max(Numbers_list))
print("Minimum value in the list is: ", min(Numbers_list))

#  Write a Python program that takes a sentence as input and prints the frequency of each word.

sentence = input("Enter the sentence for which you would like to know the frequency of the words: ").split()
frequency_word = 0
for idx, item in enumerate(sentence[0:]):
    #print(idx, item)
    for i in sentence[idx+1:]:
        if item == i:
            frequency_word += 1 
        print(f"{item} : {frequency_word}")


#  Write a Python program to check if a string is a palindrome.
string = input("Enter the word for which you like to find its a palindrom or not: ")
if string == string[::-1]:
    print("it is a palindrom")
else: 
    print("it is not a palindrom")

# Write a Python program where the user enters a sentence, and the program counts the frequency of each letter in the sentence. Store the results in a dictionary and print it.

# character as key and frequency as value.
dictionory = {}
sentence = input("Enter the sentence: ")
for item in sentence:
    if item in dictionory:
        dictionory[item] +=1 
    else :
        dictionory[item] =1 
for item, frequency in dictionory.items():
    print(f"{item} : {frequency}" )


# Write a Python program that takes a sentence as input and counts the frequency of each word.
dictionary = {}
sentence = input("enter the sentence: ").lower().split()
for item in sentence:
    if item in dictionary:
        dictionary[item] += 1
    else:
        dictionary[item] = 1
    
for item, frequency in dictionary.items():
    print(f"{item} : {frequency}") 

# Write a Python program that takes a string input and counts the number of vowels (a, e, i, o, u) in it.

frequency = 0
sentence = input("Enter the sentence: ").lower()
vowels = "aeiou"
frequency = sum (1 for item in sentence if item in vowels)
print(f"Number of Vowels: {frequency}")

#Find the Second Largest Number in a List

number_list = list(map(int, input("Enter the number: ").split()))
larger_number = sorted(set(number_list), reverse=True) 
print(f"Second largest number is: {larger_number[1]}")


#  Write a Python program that takes a list of numbers as input and finds the most frequently occurring number along with its frequency.

number_list = list(map(int, input("Enter the number: ").split()))
frequency_list = {}
for item in number_list:
    if item in frequency_list:
        frequency_list[item] += 1
    else:
        frequency_list[item] = 1
print(frequency_list)

most_frequent = max(frequency_list, key=frequency_list.get)
highest_frequency = frequency_list[most_frequent]

print(f"Most frequently occuring number is {most_frequent} with {highest_frequency} occurance")

# Find the Second Most Frequent Number in a List
number_list = list(map(int, input("Enter the number: ").split()))
dictinoray = {}
for item in number_list:
    if item in dictinoray:
        dictinoray[item] += 1
    else:
        dictinoray[item] = 1
print(dictinoray)
sorted_dictinory = sorted(dictinoray, key =dictinoray.get, reverse= True)
if len(sorted_dictinory) > 1:
    print(f"Second most frequent number is: {sorted_dictinory[1]}")
else:
    print("No second most frequent number found.") 


# Write a lambda function to multiply two numbers.
#lambda is used to create one line function without using def

multi = lambda x,y: x*y
print(multi(8,5))

# multiply every number in the list by 2
# Apply a function to each item in an iterable (like a list).

numbers = [1, 2, 3, 4, 5]
multi = list(map(lambda x: x*2, numbers))
print(multi)

# Get even numbers from a list.
# filter element based on the condition
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"even_numbers are :{even_numbers}")

# Reduce a list to a single value by applying a function cumulatively.
# Find the product of all elements in a list.

from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x,y: x*y, numbers)
print(product)

#  Given a list of temperatures in Celsius, convert them to Fahrenheit using map() and lambda.
# Formula: F = (C × 9/5) + 32

temperatures_celsius = [0, 10, 20, 30, 40]
Fahrenheit = list(map(lambda x: (x * 9/5) + 32, temperatures_celsius))
print(Fahrenheit)

# Given a list of numbers, use filter() and lambda to keep only the numbers greater than 50.

numbers = [10, 55, 30, 75, 42, 90, 15]
greater_than_fifty = list(filter(lambda x: x >50, numbers))
print(greater_than_fifty)

# Use reduce() and lambda to find the sum of all numbers in a list.

from functools import reduce
numbers = [5, 10, 15, 20]
sum_all = reduce(lambda x, y: x + y, numbers)
print(sum_all)

# Write a Python program that takes a list of numbers and uses list comprehension to create a new list containing only the even numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = [item for item in numbers if item % 2==0]
print(even)

# Use Dictionary Comprehension to Count Word Frequency
# standard
sentence = ("apple banana apple orange banana apple").split()
frequency = {}
for item in sentence:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1
print(frequency)

# dictonary comprehension

frequency = {word: sentence.count(word) for word in set(sentence)}
print(frequency)

#  Write a Python program that takes a list of numbers and creates a set containing only the squares of unique numbers using set comprehension.

numbers = [1, 2, 2, 3, 4, 4, 5]
squares = {num * num for num in numbers}
print(squares)

# Write a Python program that takes a list of words and creates a dictionary where keys are the words and values are their lengths.

words = ["apple", "banana", "orange"]

lengths = {word : len(word) for word in words}
print(lengths)

# Write a dictionary comprehension to swap keys and values in a dictionary.

fruit_colors = {'apple': 'red', 'banana': 'yellow', 'grape': 'purple'}
swap = {num: item for item, num in fruit_colors.items()}
print(swap)

# Give the count of numbers above 20

number = [1,2,3,10,20,40,50]
count = [item for item in number if item > 20]
print(len(count))

# Create new list which Multiply each item in the list with 2

number = [1,2,3,10,20,40,50]
multiple = [item * 2 for item in number]
print(multiple)



sentence = "I like 10 python".split()
dictinoray = {word: len(word) for word in sentence if word.isalpha()}
print(dictinoray)"""


# generate 100 random numbers 
# count how many are above 20
# create a table