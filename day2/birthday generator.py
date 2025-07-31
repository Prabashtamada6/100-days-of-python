from datetime import datetime

# Get the current date
today = datetime.today()
current_year = today.year
current_month = today.month

# Get user input
year = int(input("What year were you born? "))
month = int(input("What month were you born? (1-12) "))

# Calculate age
years = current_year - year
months = current_month - month

# Adjust if birth month is ahead of current month
if months < 0:
    years -= 1
    months += 12

print(f"Your age is {years} years and {months} months.")
