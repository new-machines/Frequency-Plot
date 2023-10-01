import csv
from datetime import datetime

# Function to calculate time intervals in hours as decimal fractions
def calculate_time_intervals(timestamps):
    intervals = []
    for i in range(len(timestamps) - 1):
        current_time = datetime.strptime(timestamps[i], '%Y-%m-%d %H:%M:%S')
        next_time = datetime.strptime(timestamps[i + 1], '%Y-%m-%d %H:%M:%S')
        time_difference = (next_time - current_time).total_seconds() / 3600.0
        intervals.append(time_difference)
    return intervals

# Read timestamps from timestamps.csv
timestamps = []
with open('timestamps.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        timestamps.extend(row)

# Calculate time intervals
intervals = calculate_time_intervals(timestamps)

# Write intervals to intervals.csv (overwrite existing file)
with open('intervals.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Interval (hours)'])
    for interval in intervals:
        writer.writerow([interval])