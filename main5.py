n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

if str(n1) == str(n1)[::-1] and str(n2) == str(n2)[::-1]:
    print("The both numbers are palindromes")
elif str(n1) == str(n1)[::-1]:
    print("The first number is a palindrome")
elif str(n2) == str(n2)[::-1]:
    print("The second number is a palindrome")
else:
    print("Neither number is a palindrome")