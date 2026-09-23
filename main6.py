n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))

if n1 % 10 == 1:
    print(n1, "hryvnia")
elif n1 % 10 in [2, 3, 4]:
    print(n1, "hryvni")
else:
    print(n1, "hryven")

if n2 % 10 == 1:
    print(n2, "hryvnia")
elif n2 % 10 in [2, 3, 4]:
    print(n2, "hryvni")
else:
    print(n2, "hryven")

if n3 % 10 == 1:
    print(n3, "hryvnia")
elif n3 % 10 in [2, 3, 4]:
    print(n3, "hryvni")
else:
    print(n3, "hryven") 