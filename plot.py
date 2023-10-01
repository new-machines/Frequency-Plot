import csv
import matplotlib.pyplot as plt
import numpy as np

# Read intervals from intervals.csv
intervals = []
with open('intervals.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        intervals.append(-float(row[0]))  # Make interval values negative

# Create x-axis values (indices of intervals)
x_values = range(1, len(intervals) + 1)

# Plot the intervals
plt.figure(figsize=(10, 6))
plt.scatter(x_values, intervals, marker='o', color='blue', label='Intervals')
plt.xlabel('Order in intervals.csv')
plt.ylabel('Interval (hours)')
plt.title('Time Intervals Plot')

# Perform linear regression
x = np.array(x_values)
y = np.array(intervals)
coefficients = np.polyfit(x, y, 1)
linear_regression = np.poly1d(coefficients)
regression_line = linear_regression(x)

# Plot the linear regression line
plt.plot(x, regression_line, color='red', linestyle='--', label='Linear Regression')

# Calculate the slope of the linear regression line
slope = coefficients[0]

# Display the slope value on the plot at a specific location
plt.text(1, min(intervals) * 0.9, f'Slope: {slope:.2f}', fontsize=12, color='green')

plt.grid(True)
plt.legend()
plt.show()