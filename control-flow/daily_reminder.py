task = input("Enter your task:")
priority = input("Priority(high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")
# Initialize the reminder message
reminder = f"Reminder:'{task}'"

match priority:
    case 'high':
        reminder += "is a high-priority task"
    case 'medium':
        reminder += "is a medium-priority task."
    case 'low':
        reminder += "is a low-priority task."
    case _:
        reminder += "Priority level not recognized."

if time_bound == 'yes':
    reminder += "that requires immediate attention today!"
else:
    reminder += "Consider completing it when you have free time."

print(reminder)
    

    
