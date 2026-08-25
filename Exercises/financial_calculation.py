present_value = 5000
interest_rate = 0.10
periods = 50

future_value = present_value * (1 + interest_rate) ** periods

print("Present value:", present_value)
print("Interest rate:", interest_rate)
print("Periods:", periods)
print("Future value:", round(future_value, 2))

#I decided to change the values to higher values to see how the future value changes.
#I was able to see that the future value increases significantly with higher present values,
#interest rates, and periods.
