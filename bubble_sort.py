number=[23,5,1,5,78,2]
l=len(number)
print(l)
for i in range(l):
    swap=False
    for j in range(l-i-1):
        if number[j] > number[j+1]:
            number[j],number[j+1]=number[j+1],number[j]
            swap=True
            if swap==False:
        
                print(number)
            print(number)
