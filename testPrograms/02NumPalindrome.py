
# WAP to check if a number is palindrome of not?

number = int(input("Enter the number to check for palindrome: "))

temp = number

reverse = 0

while number > 0:
    digit = number%10
    reverse = reverse*10 + digit
    number = number//10

if temp == reverse:
    print("Number is palindrome")
else:
    print("Number is not plaindrome")
