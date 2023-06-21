t = (2.0, 'python', 50, 'h', '10', 's')
print(t[1:6])
print(t[0:4])
print(t[2:])
l = list(t)
l1 = ['ranchi', 9, 8, 3.33, 4+2j]
l.extend(l1)
print(l)
if 4 in l :
    print("4 is in list.")
else :
    print("4 is not in the list")
