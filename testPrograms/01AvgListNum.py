
# WAP to calculate the average of numbers in a given listself.

listSize = int(input("Enter the listsize first: "))

myList = []


for i in range(0, listSize): #range provide 0...range from 0 to certain number
    myNum = int(input("Enter the number: "))
    myList.append(myNum)

average = sum(myList)/listSize

print("Average of this list is: ", round(average, 2)) #2 is till how many decimal places u want to round
