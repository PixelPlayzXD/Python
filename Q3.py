num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
largest = num1
smallest = num1

if num2 > largest:
    largest = num2
else:
    smallest = num2
if num3 > largest:
    largest = num3
else:
    smallest = num3
print("Largest number:", largest)
print("Smallest number:", smallest)
