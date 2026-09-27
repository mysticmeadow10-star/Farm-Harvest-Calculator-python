#A Python program that tracks a farmer's harvest across 5 fields. You will calculate the total and average yield, pack the harvest into 25 kg bags, find the leftover grain, compare this year's harvest with last year's, and update the total with a bonus crop and seed reserve.

f1 = float(input("Enter Field 1  harvest (kg):"))
f2 = float(input("Enter Field 2  harvest (kg):"))
f3 = float(input("Enter Field 3  harvest (kg):"))
f4 = float(input("Enter Field 4  harvest (kg):"))
f5 = float(input("Enter Field 5  harvest (kg):"))

total = f1 + f2 + f3 + f4 + f5
average = total/5

print(f"Total Yield : {total} kg")
print(f"Average Yield : {average} kg")

bags = total//25
leftover = total%25

print(f"Full 25kg bags packed: {bags}")
print(f"leftover grain: {leftover}")

last_year = float(input("Enter last year's total harvest (kg):"))
if total > last_year:
    print("Great Job! This year's harvest is higher than last year.")
elif total < last_year:
    print("This year's harvest is lower than last year.")
else:
    print("This year's harvest is same as last year.")

bonus = float(input("Enter bonus crop to add (kg):"))
seed = float(input("Enter seed reserve to remove (kg):"))

total += bonus
total -= seed

print(f"Final updated total harvest:{total} kg")