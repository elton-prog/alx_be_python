from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format and print the current date and time
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date(days):
    # Calculate the future date
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    # Print the future date
    print("Future date:", future_date.strftime("%Y-%m-%d"))

# Part 1: Display the current date and time
display_current_datetime()

# Part 2: Calculate a future date
try:
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(days_to_add)
except ValueError:
    print("Please enter a valid integer for the number of days.")