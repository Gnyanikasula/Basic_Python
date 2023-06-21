a = set()
b = set()
c = True
d = True
while c:
    a.add(int(input("Enter for A:")))
    s = input("To Continue filling;Enter: y or n :")
    if s == 'y':
        c = True
    else :
        c = False
while d:
    b.add(int(input("Enter for B:")))
    s = input("To Continue filling;Enter: y or n :")
    if s == 'y':
        d = True
    else :
        d = False     
u_set = a | b
i_set = a & b
print("Union:")
print(u_set)
print("\nIntersection:")
print(i_set)           