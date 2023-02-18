student = {}
length = int(input("Enter number of students: "))
for i in range(length):
    print("\n-----Student {}-----".format(i+1))
    roll = int(input("Enter roll number of student: "))
    name = input("Enter name of the student: ")
    marks = int(input("Enter marks of the student: "))
    student[roll] = [name,marks]
print("\n*****Student Details*****")
print(student)
print("\nStudents with marks over 75:")
for i in student:
    if student[i][1] > 75:
        print(student[i][0])
