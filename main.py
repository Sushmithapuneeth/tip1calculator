
print("Welcome to the tip calculator!")
Bill_amount = float(input("What was the total bill?\n $"))
TIP = int(input("What percentage tip would you like to give? 10, 12  or 15?\n"))
Split = int(input("How many people to split the bill?\n"))

tip_amount = (TIP * Bill_amount)/100

Pay_amount = (Bill_amount + tip_amount)/Split

final_amount = round(Pay_amount, 2)

print(f"Each person should pay : ${final_amount} dollar")