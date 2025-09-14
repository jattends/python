"""s = "malayalam"  # string

i,j = 0, len(s) - 1  # two pointers

is_palindrome = True  # assume palindrome
while i < j:
    if s[i] != s[j]:  # mismatch found
        is_palindrome = False
        break
    i += 1
    j -= 1

if is_palindrome:
    print("Yes")
else:
    print("No")"""
#armstrong
s=input("enter a string")
i,j = 0,len(s)-1
is_palindrome = True
while i<j:
    if s[i]!=s[j]:
        is_palindrome = False
        break
    i += 1
    j -= 1
if is_palindrome:
    print("yes")
else:
    print("no")
print(s)



















