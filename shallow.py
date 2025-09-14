#shallow copy : shared the two list and copy them
import copy
d=[12,13,14,15]
x=copy.copy(d)
x[2]=19
print(x)
print(d)
#deep copy :cannot sharing the the two list .its itsv suprate another file