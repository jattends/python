a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))
m=int(str(a)+str(b)+str(c))
d=a**3+b**3+c**3
if m==d:
    print("its armstrong")
else:
    print("its not armstrong")