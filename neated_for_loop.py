rows=5
for r in range(1,rows+1):
    num=r
    s=rows-1
    for c in range(1,r+1):
        print(num,end=" ")
        num+=s
        s-=1
    print(" ")