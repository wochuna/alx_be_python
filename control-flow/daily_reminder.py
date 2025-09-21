task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += "."
    case "medium":
        reminder = f"'{task}' is a medium priority task"
        if time_bound == "yes":
            reminder += " try to get it done soon!"
        else:
            reminder += " consider completing it when you have some time."
    case "low":
        reminder = f"'{task}' is a low priority task."
        if time_bound == "yes":
            reminder += " but you should still try to finish it today!"
        else:
            reminder += " Consider completing it when you have free time."
    case _:
        reminder = "Invalid priority level entered. Please enter high, medium, or low."

print(reminder)