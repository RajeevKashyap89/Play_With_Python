print("Calculate Tip!! for your Dining!!!")
bill = float(input("What is the total bill amount?\n$:"))
tip = int(input("how much tip would you like to give?\n Percent: "))
split = int(input("How many people are to split the bill?\n No_Of_People:"))

total = (((bill * (tip / 100)) + bill) / split)

print(f"Each person should pay ${total: .02f}")
