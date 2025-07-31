print("Welcome to the tip calculater!")
bill=float(input("what was the total bill: $"))
tip=int(input("how much tip would you like to give? 10, 12, or 15?: "))
people=int(input("how many people to split the bill: "))
percentage=tip/100+1
total_bill=bill * percentage
each_person=total_bill/people
final_amount=round(each_person,2)
print(f"each person should pay: ${final_amount}")
