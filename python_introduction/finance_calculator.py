# User Input for Financial Details
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate Monthly Savings
monthly_savings = monthly_income - monthly_expenses

# Project Annual Savings with 5% interest
annual_savings = monthly_savings * 12  # Savings for 12 months
projected_savings = annual_savings + (annual_savings * 0.05)  # Adding 5% interest

# Output Results
print(f"Your monthly savings are: ${monthly_savings:.2f}")
print(f"Your projected annual savings (with 5% interest) are: ${projected_savings:.2f}")
