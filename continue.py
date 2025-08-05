while True:
 a=int(input("enter your first number :"))
 b=int(input("enter your second number :"))
 print("1.addition\n2.substraction\n3.multipilcation\n4.division")
 choice=int(input("enter your choice number :"))
 match choice:
        case 1:
            print(a+b)
        case 2:
            print(a-b)
        case 3:
            print(a*b)
        case 4:
            print(a/b)
        case __:
            print("invalid choice")
            continue
 again = input("do you want to continue? (yes/no)")
 if again !="yes":
     break





