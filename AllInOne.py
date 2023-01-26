while True:
    choice = int(input("Enter Your Choice (1 - 10 / 0 to exit): "))
    if choice == 0:
        print("Exiting...")
        break
    elif choice == 1:
        print("Program to input a welcome message and print it.")
        welcome = input("Enter a welcome message: ")
        print(welcome)
    elif choice == 2:
        print("Program to input two numbers and display larger and smaller using if")
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        if num1 > num2:
            print(num1, "is the larger number")
            print(num2, "is the smaller number")
        else:
            print(num2, "is the larger number")
            print(num1, "is the smaller number")
    elif choice == 3:
        print("Program to I=input three numbers and display the larger and smaller using if-elif")
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
    elif choice == 4:
        print("Program to compute X raised to N using while loop")
        x = int(input("Enter a value for X: "))
        n = int(input("Enter a value for N: "))
        power = 1
        for i in range(0,n):
            power *= x
        print("X raised to N is:", power)
    elif choice == 5:
        print("""Program to input the values of X and N and print the sum of the following series
    -X + (X^2 / 2!) - (X^3 /3!) + . . . + (X^N /N!)""")
        x = -1 * int(input("Enter the value for X: "))
        n = int(input("Enter the value for N: "))
        total = 0
        for i in range(1,n+1):
            fact = 1
            for j in range(1,i+1):
                fact *= j
            total += (x**i)/fact
        print("The sum of the series is:", total)
    elif choice == 6:
        print("Menu driven program to determine whether a number is a Perfect number, Amstrong number or a Palindrome number")
        print("""1. Perfect Number
2. Armstrong Number
3. Palindrome Number
4. Exit""")
        while True:
            choice = int(input("What do you want to do (1 - 4): "))
            if choice == 1:
                num = int(input("Enter a number: "))
                total = 0
                for i in range(1, num):
                    if num % i == 0:
                        total += i
                if total == num:
                    print(num, "is a perfect number!")
                else:
                    print(num, "is a not a perfect number!")
            elif choice == 2:
                num = int(input("Enter a number: "))
                if num < 0:
                    print(num, "is a not an armstrong number!")
                else:
                    temp = num
                    length = 0
                    while temp > 0:
                        temp //= 10
                        length += 1
                    temp = num
                    total = 0
                    while temp > 0:
                        digit = temp % 10
                        total += digit ** length
                        temp //= 10
                    if total == num:
                        print(num, "is an armstrong number!")
                    else:
                        print(num, "is a not an armstrong number!")
            elif choice == 3:
                num = int(input("Enter a number: "))
                temp = num
                reverse = 0
                while temp > 0:
                    digit = temp % 10
                    reverse = reverse * 10 + digit
                    temp //= 10
                if num == reverse:
                    print(num, "is a palindrome number!")
                else:
                    print(num, "is a not a palindrome number!")
            elif choice == 4:
                break
            else:
                print("Enter a valid option!")
    elif choice == 7:
        print("Program to input a number and find if its prime or composite")
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
    elif choice == 8:
        print("Program to display the terms in Fibonacci series to N terms ")
        n = int(input("Enter the limit: "))
        a = 0
        b = 1
        for i in range(n):
            print(a, end=', ')
            c = a + b
            a = b
            b = c
    elif choice == 9:
        print("Program to compute the greatest common divisor and least common multiple of any two numbers")
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
    elif choice == 10:
        print("Program to count and display the number of letters, vowels, consonants, uppercase, lowercase characters in a string")
        vowel = 0
        consonant = 0
        upper = 0
        lower = 0
        letter = 0
        string = input("Enter a string: ")
        for i in string:
            if not i.isspace():
                letter += 1
            if i.isupper():
                upper += 1
            if i.islower():
                lower += 1
            if i in "aeiouAEIOU":
                vowel += 1
            if i.isalpha() and i not in "aeiouAEIOU":
                consonant += 1
        print("""Number of letters: {}
Number of upper case letters: {}
Number of lower case letters: {}
Number of vowels: {}
Number of consonants: {}""".format(letter, upper, lower, vowel, consonant))
