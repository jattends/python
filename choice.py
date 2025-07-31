a=int(input("enter a number:"))
b=int(input("enter a secobd number:"))
print("1.addition/n2.substraction/n3.mutiplication/n4.division")
choice=int(input("enter your choice:"))
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
        print("are you fool")
