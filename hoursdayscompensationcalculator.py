# This will determine what you make per day worked

inp0 = input('How many hours do you work a day?')
inp1 = input('How many days did you work?')
inp2 = input('How much do you make an hour?')
hrs = float(inp0) * float(inp1) * float(inp2)
print("Your Total Compensation for Worked Hours:", float(hrs))