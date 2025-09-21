task = input("Enter your task:")
priority = input("Priority(high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")
# Initialize the reminder message
reminder = f"Reminder: {task}."

match priority:
    case 'high':
        reminder += " This is a high-priority task."
    case 'medium':
        reminder += " This is a medium-priority task."
    case 'low':
        reminder += " This is a low-priority task."
    case _:
        reminder += " Priority level not recognized."

if time_bound == 'yes':
    reminder += " This requires immediate attention today!"

print(reminder)
    

    
