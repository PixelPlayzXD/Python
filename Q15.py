length = int(input("Enter number of elements you want to sort: "))
lst = []
for i in range(1,length+1):
    lst.append(int(input("Enter element no.{}: ".format(i))))
print("Entered list:",lst)
for i in range(length):
    for j in range(0,length-i-1):
        if lst[j] > lst[j+1]:
            lst[j],lst[j+1] = lst[j+1],lst[j]
print("Sorted list:",lst)