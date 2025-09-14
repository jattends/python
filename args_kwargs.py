#*args is uses of tuble values and non key word argument/**kwargs is uses of dictory values and itrs a keyword arguments
"""def fun(**kwargs):
    print(kwargs)
fun(name="nithanth")"""
#global=use is out side value insert
"""a=25
def fun():
    global a
    a=a+3
    print(a)
fun()
"""
"""a=50
def fun():
    global a
    a=a+30
    print(f"sum is :{a}")
fun()"""
#mapping[
"""def square(n):
    return n*n
number=[1,2,3,4,5,6]
squares=list(map(square,number))
print(squares)"""
l1=[1,2,3,4,5,6]
square=list(map(lambda x:x**2,l1))
print(square)




