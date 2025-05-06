"""user_name = input("Enter the name: ")
try: 
    user_age = int(input("Enter the age: "))
    if  0 <= user_age <= 100:
        year = (100 - user_age) + 2025
        print(f"{user_name} you will turn 100 year old in {year}")
        
    else:
        print("age not valid")

except ValueError:
    print("Invalid input, Enter a number for age") 

try:
    user_value= int(input("Enter the integer number: "))
    if user_value % 2 == 0:
        print("It is an even number")
        if user_value % 4 == 0:
            print("This number is divisible by 4")
    else:
        print("It is a odd number")

except ValueError:
    print("Invalid input, Enter the integer number")


even_list = []
odd_list = []
num = [2,3,8,9,56]  
for item in num:
    if item % 2 == 0:
        even_list.append(item)
 #print(f"{item} is a even number")
    else:
        odd_list.append(item)

 #print(f"{item} is a odd number")
print(len(even_list))
print(len(odd_list))

try:
    user_num = list(map(int, input("Enter the numbers separarted by space: ").split()))
    print(max(user_num))
    print(min(user_num))
except ValueError:
    print("Invalid input, enter the integer number")
count = 0
sentence = ("Hello I am Pradyumna").lower()
for vowel in sentence:
    if vowel in  "aeiou":
        count += 1
print(count)"

sentence = input("Enter the sentence: ").lower()
vowels = "aeiou"

frequency = {vowel:0 for vowel in vowels}

for char in sentence:
    if char in vowels:
        frequency[char]+=1
    
for vowel, count in frequency.items():
    print(f"{vowel}: {count}")


mylist = ['apple', 'banana', 'cherry']
mylist[1:3] = ['kiwi', 'mango']
print(mylist)

#list copy
list1= [1,2,5,2]
#list2 = list(list1)
#list2 = list1.copy()
#list2 = list1[:]
print(list2)

list1= [1,2,5]
list2= [8,9,6]
list1.extend(list2)
print(list1)

fruits = ('apple', 'banana', 'cherry')
(x,y,z)= fruits
print(z)


#Task: Write a function to clean a sentence by:

#Lowercasing

#Removing punctuationcdc

#Stripping extra spaces
sentence = "Hello I am Pradyumna "
def clean_txt(text):
    cleaned = text.split()
    print(cleaned)
clean_txt(sentence)"""

sentence = "I have a cat. I have a Dog. I HAve 5 chicken".split(".")
tokens = [item.split() for item in sentence]
print(tokens)

"""def to,kenize(text):
    temp = []
    for item in text:
        temp.append(item.split())
    print(temp)
tokenize(sentence)"""