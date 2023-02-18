length = int(input("Enter the number of elements you want to enter: "))
lst = []
for i in range(1,length+1):
    lst.append(int(input("Enter element no.{}: ".format(i))))
print("The list before swapping is:",lst)
if length%2!=0:
    length=length-1
for i in range(0,length,2):
    lst[i],lst[i+1] = lst[i+1], lst[i]
print("The list after swapping is:",lst)