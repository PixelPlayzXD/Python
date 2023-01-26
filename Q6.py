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