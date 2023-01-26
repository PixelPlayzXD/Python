a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
lcm = a
while True:
    if lcm % b == 0:
        break
    lcm += a
if (a*b) > 0:
    gcd = int((a*b)/lcm)
else:
    gcd = int((-1*(a*b))/lcm)
print("The Least Common Multiple of", a, "and", b, "is", lcm)
print("The Greatest Common Divisor of", a, "and", b, "is", gcd)
