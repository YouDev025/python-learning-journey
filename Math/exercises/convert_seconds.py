# Convert Seconds to Time Units


seconds = float(input("Enter the number of seconds: "))

minutes = seconds / 60
hours = minutes / 60
days = hours / 24

weeks = days / 7
months = days / 30.44   # average month length
years = days / 365.25   # accounts for leap years

print(f"\nTime conversion results:")
print(f"Seconds: {seconds:0.2f}")
print(f"Minutes: {minutes:0.2f}")
print(f"Hours: {hours:0.2f}")
print(f"Days: {days:0.2f}")
print(f"Weeks: {weeks:0.2f}")
print(f"Months (approx): {months:0.2f}")
print(f"Years (approx): {years:0.2f}")