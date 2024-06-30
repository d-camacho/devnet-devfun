#Drink tracker for ETP Night at EOP

# Initialize an empty dictionary to store the number of drinks for each badge number
drink_tracker = {}

def get_drink(badge_number):
    # Check if the badge number is valid
    if not (1 <= badge_number <= 9999):
        print("Invalid badge number. Please enter a number between 1 and 9999.")
        return

    # Get the current drink count for the badge number, defaulting to 0 if not present
    else:
        current_drinks = drink_tracker.get(badge_number, 0)

        # Check if the user has already reached the drink limit
        if current_drinks >= 2:
            print(f"Badge number {badge_number} has already reached the drink limit of 2.")
        else:
            # Increment the drink count
            drink_tracker[badge_number] = current_drinks + 1
            print(f"Drink {current_drinks + 1} recorded for badge number {badge_number}.")

def tracker():
    while True:
        try:
            # Prompt the user for their badge number
            badge_number = int(input("Please enter the badge number (1-9999): "))
            get_drink(badge_number)
        except ValueError:
            print("Invalid input. Please enter a numeric badge number.")

        # Ask if another drink should be recorded
        another = input("Would you like to record another drink? (y/n): ").strip().lower()
        if another != 'y':
            print(drink_tracker)
            break

if __name__ == "__main__":
    tracker()
