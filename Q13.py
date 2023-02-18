length = int(input("Enter the number of elements you want to enter: "))
lst = []
for i in range(1,length+1):
    lst.append(int(input("Enter element no.{}: ".format(i))))
largest = lst[0]
smallest = lst[0]
for i in lst:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i
print("The list is:",lst)
print("Largest number is the list is:",largest)
print("Smallest number is the list is:",smallest)