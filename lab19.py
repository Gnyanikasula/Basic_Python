n = int(input("Enter Number:"))
b =0
p = 0
while n>0:
    b = n%2 + b*10
    if(b == 0):
        p+=1
    n = n//2
print(b*10**p)
        