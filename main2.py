tank = float(input("Enter the amount of fuel in the car's tank (in liters): "))
percent = float(input("Enter how much fuel is in the tank (as a percentage): "))
km_per_liter = float(input("Enter how many kilometers the car can travel per liter of fuel: "))

fuel = tank * percent / 100
distance = fuel * km_per_liter

print(f"You can drive another {distance} kilometers.")
print(f"Next refueling after 200 kilometers.")

if distance >= 200:
    print("You can wait until the next refueling.")
else: 
    print("FILL IN NOW!")
