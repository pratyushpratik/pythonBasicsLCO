
# WAP to print multiplication tables of a given number


number = int(input("Enter the number for multiplication table: "))

for i in range(1, 11):
    if i == 10:
        print(number, " x ", i, "= ", (number * i))
    else:
        print(number, " x ", i, " = ", (number * i))
