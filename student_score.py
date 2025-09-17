"""# student'score

score = float(input("Enter the student's score (0-100):"))
if score >100 or score <0:
    print("enter a number between 0 and 100")
elif score > 95:
    print("Grade: A+")
    print("congratulations! you achieved a high distinction")
elif score >=85:
    print("Grade: A")
elif score >=75:
    print("Grade: B")
elif score >=65:
    print("Grade: C")
elif score >=55:
    print("Grade: D")
else:
    print("Grade: F(fail)")

# check a number is postive, negative, or zero

num=int(input("Enter the number : "))
if num >=1:
    print("Number is positive")
elif num<0:
    print("Number is negative")
else:
    print("Number is zero")

"""
from win32comext.mapi.emsabtags import PR_EMS_AB_LOCAL_INITIAL_TURN

"""#sum of 1 - 10 numbers
Total = 0
for i in range (1,10):
    Total += i
    print("sum= ",Total)

#print even number
number=[1,2,3,4,5,6,7,8,9]
for num in number:
    if num %2==0:
        print(num)

#multilplication
for i in range(1,6):
    for j in range(1,6):
        product = i*j
        print(f"{product:3}",end=" ")
    print()

#password validation
password = ""
while password != "python123":
    password = input("enter password:")
else:
    print("correct password!")

#find a number in a list

numbers = [1, 2, 3, 4, 5]
target = 6

for num in numbers:
    if num == target:
        print("Number found!")
        break
else:
    print("Number not found!")"""
"""
#rectangle pattern printing
for i in range(4):
    for j in range(6):
     print("*",end=" ")
    print()
#square pattern printing
for i in range(5):
 for j in range(5):
     print("*",end="  ")
 print()
#pyramid
for i in range(5,0,-1):
    for j in range(1,i + 1):
        print(j,end=" ")
    print()"""
#function using calculate total tax
"""def calculate_total(price,tax=5):
    return price + (price * tax/100)
print(calculate_total(100))

"""
#adding items using global varble
"""item=[]
def add_items():
    global item
    item.append("apple")
add_items()
print(item)"""

"""#string reverse
def reverse_string(s):
 if len(s)==0:
     return s
 else:
     return reverse_string(s[1:]) + s[0]
print(reverse_string("hello"))"""
"""#lambda function
square = lambda n: n*n
print(square(5))"""
"""#favorite food using for loop
favorite_food=["burger","mandi","meals","beef curry","chicken curry"]
for food in favorite_food:
    print(f"I love eating {food}")"""
"""#square for numbers
squares = [x**2 for x in range(1,11)]
print(squares)"""
"""#vowel string
text = 'Python Programming is fun!'
vowels = [char for char in text if char.lower() in 'aeiou']
print(vowels)"""
"""#even numbers
for num in range(1,21):
    if num % 2 == 0:
        print(num)"""
"""#extract python
text = "programing"
print(text[0],text[-1])

#reverse a string
text = "programming"
reversed_text = text[::-1]
print(reversed_text)

#specific character
text = "malayalam"
print(text.count("m"))

#spaces with underscores
sentence = "python is fun to learn"
print(sentence.replace(" ","_"))

#pailndrome
word = "madam"
print(word == word[::-1])
"""
#zip()
students = ["Alice", "Bob", "Charlie"]
grades = [85, 92, 78]

student_grades = dict(zip(students, grades))
print(student_grades)

#two lists of numbers
list1 = [10, 20, 30]
list2 = [1, 2, 3]

sums = [a + b for a, b in zip(list1, list2)]
print(sums)

#Unzip a zipped object into individual lists.

# Zipped object
zipped = zip([1, 2, 3], ['a', 'b', 'c'])

# Unzipping
numbers, letters = zip(*zipped)

# Convert back to lists (optional)
numbers = list(numbers)
letters = list(letters)

print(numbers)  # [1, 2, 3]
print(letters)  # ['a', 'b', 'c']
