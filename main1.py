# This program calculates the average of tree points and prints a message if the average is greater than 95.
n1 = int(input("Enter your point1: "))
n2 = int(input("Enter your point2: "))
n3 = int(input("Enter your point3: "))

average = (n1 + n2 + n3) / 3
print(f"{average:.2f}")
if average > 95:
    print("Congratulations! That is a great average!")
