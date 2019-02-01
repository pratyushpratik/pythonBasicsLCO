# WAP to merge two lists and sort it


mylist1 = []
mylist2 = []

listsize1 = int(input("Enter list size for list 1: "))
for i in range(0, listsize1):
    element1 = int(input("Enter elements for list1: "))
    mylist1.append(element1)


listsize2 = int(input("Enter list size for list 2: "))
for i in range(0, listsize2):
    element2 = int(input("Enter elements for list2: "))
    mylist2.append(element2)


mergelist = mylist1 + mylist2

mergelist.sort()

print("Your new sorted list is: ", mergelist)
