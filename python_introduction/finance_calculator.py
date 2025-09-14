monthly_income = float(input("please enter your monthly income :"))
monthly_expenses = float(input("enter your total monthly expenses :"))

monthly_saving = monthly_income - monthly_expenses
print(f"monthly savings are {monthly_saving}")
rate = 0.05

projected_saving = monthly_saving * 12 + (monthly_saving * 12 * rate)
print(f"projected saving after one year with interest is : {projected_saving}")