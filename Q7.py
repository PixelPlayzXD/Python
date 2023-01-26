num = int(input("Enter a number: "))
prime = True
if num == 1:
    prime = False
for i in range(2, num):
    if num % i == 0:
        prime = False
if prime:
    print(num, "is a prime number!")
else:
    print(num, "is a composite number!")
