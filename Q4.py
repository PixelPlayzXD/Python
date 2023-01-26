x = int(input("Enter a value for X: "))
n = int(input("Enter a value for N: "))
power = 1
for i in range(0,n):
    power *= x
print("X raised to N is:", power)
