h = float(input("Enter Height in CM?"))
r = float(input("Enter Radius in CM:"))

volume = round(3.14*r**2*h,2)
csa = round(2*3.14*r*h,2)
tsa = round(2*3.14*r*(h+r),2)
ba = round(3.14*r**2,2)

print(f"Base Area of Cylinder is:{ba}")
print(f"CSA of Cylinder is: {csa}")
print(f"TSA of cylinder is :{tsa}")
print(f"Volume of cylinder is :{volume}")

