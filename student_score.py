# student'score

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

