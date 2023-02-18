employ = {}
while True:
    opt = input("""\n*****MENU*****
\t1. Add an employee
\t2. Display employee details
\t3. Search an employee
\t4. Exit
Enter an option (1 - 4): """)
    if opt == "1":
        print("\n--------------------")
        eno = int(input("Enter employee number: "))
        name = input("Enter employee name: ")
        desig = input("Enter employee designation: ")
        salary = input("Enter employee salary: ")
        employ[eno] = [name,desig,salary]
        print("Enployee details successfully added!")
    elif opt == "2":
        print("\----------Employee Details----------")
        print(employ)
    elif opt == "3":
        sno = int(input("Enter employee number to search: "))
        for i in employ:
            if i == sno:
                print(employ[i])
            else:
                print("Employee not found")