print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
num_people = int(input("How many people to split the bill? "))
tip_percent = int(input("What percentage tip would you like to give? "))
per_person = (total_bill / num_people) + ((total_bill / num_people)*(tip_percent/100))
final_amount = "{:.2f}".format(per_person)
print(f"Each person should pay: ${final_amount}")