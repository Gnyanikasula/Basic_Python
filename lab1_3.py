a = int(input("Enter Number 1:"))
b = int(input("Enter NUmber 2:"))

# without temporary variable
a = a+b
b = a-b
a = a-b
print(f"Swaped without temporary variable {a} {b}") 

# With Temporaray

temp = a
a = b
b = temp 
print(f"Swaped with Temp and retained original: {a} {b}")
