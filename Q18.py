length = int(input("Enter number of elements you want to enter: "))
lst = []
for i in range(1,length+1):
    lst.append(int(input("Enter element no.{}: ".format(i))))
print("Entered list:",lst)
print("Armstrong numbers: ",end="")
for i in range(length):
    copy = lst[i]
    tot = 0
    while copy > 0:
        rem = copy%10
        tot += rem**3
        copy //= 10
    if tot == lst[i]:
        print(lst[i],end=" ")
print("\nSmallest element in the list:",min(lst))
print("Largest element in the list:",max(lst))