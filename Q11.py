while True:
    opt = input("""\t*****Menu*****
\t1.Palindrome
\t2. Convert Case
Enter an option (1/2): """)
    if opt == "1":
        string = input("Enter a string: ")
        string2 = string.upper()
        if string2 == string2[::-1]:
            print(string,"is a palindrome!")
        else:
            print(string,"is not a palindrome!")
    elif opt == "2":
        string = input("Enter a string: ")
        print("String after changing case: ",end="")
        for i in string:
            if i.isupper():
                print(i.lower(),end="")
            elif i.islower():
                print(i.upper(),end="")
            else:
                print(i,end="")
        print()
    else:
        print("Enter a valid option!")
    proceed = input("\nDo you want to continue (Y/N): ").upper()
    if proceed != "Y":
        break
