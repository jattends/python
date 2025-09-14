list1=[12,"nithanth",16,"harsha"]
list2=[13,"sourav",20,"surya"]
s=list(zip(list1,list2))
print(s)
#using zip* : unziping
list1=[12,"nithanth",16,"harsha"]
list2=[13,"sourav",20,"surya"]
s=list(zip(list1,list2))
l1,l2=zip(*s)
print(l1,l2)


