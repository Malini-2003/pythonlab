import numpy as np

monthly_expenses = np.array([1500, 200, 250, 100])

total_monthly = np.sum(monthly_expenses)
total_yearly = total_monthly * 12

print(f"Total monthly expense: ${total_monthly:.2f}")
print(f"Total yearly expense: ${total_yearly:.2f}")
