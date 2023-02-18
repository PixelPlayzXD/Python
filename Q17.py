length = int(input("Enter number of elements you want to sort: "))
tup = ()
for i in range(1,length+1):
    tup += (int(input("Enter element no.{}: ".format(i))),)
print("Entered tuple:",tup)
lst = list(tup)
for i in range(1,length):
    temp = lst[i]
    j = i-1
    while (j >=0 and temp > lst[j]):
        lst[j+1] = lst[j]
        j = j-1
    lst[j+1] = temp
print("Sorted tuple:",tuple(lst))