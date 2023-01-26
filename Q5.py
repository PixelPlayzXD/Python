# -X + (X^2 / 2!) - (X^3 /3!) + . . . + (X^N /N!)
x = -1 * int(input("Enter the value for X: "))
n = int(input("Enter the value for N: "))
total = 0
for i in range(1,n+1):
    fact = 1
    for j in range(1,i+1):
        fact *= j
    total += (x**i)/fact
print(total)