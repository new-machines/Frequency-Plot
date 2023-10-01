import csv
from datetime import datetime

# Function to write or append a timestamp to the CSV file
def write_timestamp_to_csv():
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open('timestamps.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp])

if __name__ == "__main__":
    write_timestamp_to_csv()