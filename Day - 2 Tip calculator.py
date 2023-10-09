# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇
print("Welcome to tip calculator!!")
total_bill = input("What was the total bill? ")
tip = input("How much percentage would you like to tip 10, 12 or 15. ")
split = input("How many people split the bill. ")
t_b = float(total_bill)
t = int(tip)
s = int(split)
x = t / 100
y = t_b * x
z = y + t_b
r = (z / s)
result = round(r, 2)
print(f"Each person should pay {result}")
