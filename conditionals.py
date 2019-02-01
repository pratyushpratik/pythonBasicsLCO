

#bill_amount = 700

bill_amount = int(input("Enter the bill amount:"))

if bill_amount < 500:
    discount = bill_amount*0.05
    print("Discount amount is: ", discount)
else:
    discount = bill_amount*0.10
    print("Discount amount is: ", discount)

print("Your final amount is: ", bill_amount-discount)
