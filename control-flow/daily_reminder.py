# Prompt the user for task details
task = input("Enter the task description: ")
priority = input("Enter the task’s priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()

match priority:
    case "high":
        reminder = f"The task '{task}' has a high priority."
    case "medium":
        reminder = f"The task '{task}' has a medium priority."
    case "low":
        reminder = f"The task '{task}' has a low priority."
    case _:
        reminder = f"The task '{task}' has an unknown priority."

if time_bound == "yes":
    reminder += " It requires immediate attention today!"

print(reminder)
