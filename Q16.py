t = ()
length = int(input("Enter the number of elements you want to enter: "))
for i in range(length):
    t += (int(input("Enter element no.{}: ".format(i+1))),)
element = int(input("Enter element to search: "))
for i in range(length):
    if t[i] == element:
        print(element,"found at index",i)
        break
else:
    print(element,"not found in the tuple")