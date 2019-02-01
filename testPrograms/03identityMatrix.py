
# WAP for identity matrix


matsize = int(input("Enter size of matrix: "))

for row in range(0, matsize):
    for column in range(0, matsize):
        if row == column:
            print("1", sep=' ', end=' ')
        else:
            print("0", sep=' ', end=' ')
    print()
