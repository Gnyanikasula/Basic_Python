sp =[]
cp =[]
q = []
c = True
while c:
    cp.append(int(input("Enter cp:")))
    sp.append(int(input("Enter SP:")))
    
    q.append(int(input("Enter Quantity:")))
    s = input("Do you want to enter more?\n y or n:")
    if s == 'y':
        c = True
    else :
        c = False
ssp = 0
scp = 0        
for x in cp :
    for y in q:
        scp = scp + x*y
for x in sp :
    for y in q:
        ssp = ssp + x*y        
d =  round((ssp-scp)/100,2)
if d>=10:
    print(f"Profit :{d}%")
elif d <= -10 :
    print(f"Lose : {d}%")
else :
    print("Average")    
        