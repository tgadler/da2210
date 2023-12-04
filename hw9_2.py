import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0) 
lambda_rate = 300  # Average number of visitors per day
num_days = 365 * 5  # Simulate for 5 years
daily_visitors = []

for _ in range(num_days):
    time = 0
    visitors = 0
    while time < 1:  # Simulate one day
        time += np.random.exponential(1/lambda_rate)
        if time < 1:
            visitors += 1
    daily_visitors.append(visitors)

# Time series plot
plt.figure(figsize=(15, 5))
plt.plot(daily_visitors, label='Daily Visitors')
plt.xlabel('Day')
plt.ylabel('Number of Visitors')
plt.title('Time Series of Daily Visitors')
plt.legend()
plt.show()

# Histogram
plt.figure(figsize=(10, 6))
plt.hist(daily_visitors, bins=range(min(daily_visitors), max(daily_visitors) + 1, 1), density=True)
plt.xlabel('Number of Visitors')
plt.ylabel('Frequency')
plt.title('Histogram of Daily Visitors')
plt.show()

# Calculating the p-value
p_value = sum(np.array(daily_visitors) >= 369) / num_days
print(f'P-Value: {p_value}')