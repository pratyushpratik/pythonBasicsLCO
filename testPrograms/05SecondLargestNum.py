
# WAP to find the second largest number in a listself.

listsize = int(input("Enter the size of list: "))

mylist = []

for i in range(0, listsize):
    element = int(input("Enter the element: "))
    mylist.append(element)

mylist.sort()

print("Second largest element is: ", mylist[len(mylist) - 2])
