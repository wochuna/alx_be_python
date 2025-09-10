monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
R = 5/100


monthly_savings = monthly_income - monthly_expenses

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * R)

print(f"Your monthly savings are ${monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${projected_savings}")