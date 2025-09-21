task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        print(f"Note: '{task}' is a high priority task.")
    case "medium":
        print(f"Note: '{task}' is a medium priority task. Consider completing it during your free time.")
    case "low":
        print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")


if time_bound == "yes":
    print(f"Reminder: '{task}' This task requires immediate attention today!")
