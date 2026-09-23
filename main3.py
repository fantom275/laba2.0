year1 = int(input("Enter a year: "))
month1 = int(input("Enter a month (1-12): "))
year2 = int(input("Enter another year: "))
month2 = int(input("Enter another month (1-12): "))

age = (year2 - year1) * 12 + (month2 - month1)

if month1 == month2:
    print(f"A full year has passed, {age // 12} years")
else:
    print(f"The age in years is: {age // 12} years")
