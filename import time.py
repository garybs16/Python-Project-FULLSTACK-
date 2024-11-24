import time
from datetime import datetime

# A dictionary to store reminders
reminders = {}

def add_reminder(name, reminder_time):
    """
    Add a new reminder.
    :param name: Name or description of the reminder.
    :param reminder_time: Datetime object for when the reminder is due.
    """
    reminders[name] = reminder_time
    print(f"Reminder '{name}' set for {reminder_time}.")

def check_reminders():
    """
    Check for reminders that are due and print them.
    """
    current_time = datetime.now()
    due_reminders = [name for name, time in reminders.items() if time <= current_time]

    for name in due_reminders:
        print(f"Reminder: {name} is due!")
        # Remove the reminder after notifying
        del reminders[name]

def display_reminders():
    """
    Display all current reminders.
    """
    if reminders:
        print("Current Reminders:")
        for name, time in reminders.items():
            print(f"  - {name}: {time}")
    else:
        print("No reminders set.")

def main():
    print("Welcome to the Reminder App!")
    while True:
        print("\nOptions:")
        print("1. Add Reminder")
        print("2. View Reminders")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter reminder name: ")
            date_str = input("Enter date and time for reminder (YYYY-MM-DD HH:MM:SS): ")

            try:
                reminder_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
                add_reminder(name, reminder_time)
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD HH:MM:SS.")
        
        elif choice == '2':
            display_reminders()

        elif choice == '3':
            print("Exiting Reminder App. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please choose again.")
        
        # Check for due reminders
        check_reminders()
        time.sleep(1)  # Delay to prevent constant CPU usage

if __name__ == "__main__":
    main()
