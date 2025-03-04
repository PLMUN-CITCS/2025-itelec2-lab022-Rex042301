def display_menu() -> None:
    """
    Displays the menu options to the user.
    No parameters.
    """
    print("\nMenu:")
    print("1. Greet User")
    print("2. Check Even/Odd")
    print("3. Exit")


def greet_user() -> None:
    """
    Greets the user with a welcome message.
    No parameters.
    """
    print("Hello! Welcome!")


def even_odd_checker_action() -> None:
    """
    Prompts the user to enter an integer and checks if it is even or odd.
    No parameters.
    """
    try:
        number = int(input("Enter an integer: "))
        if number % 2 == 0:
            print(f"{number} is an Even number.")
        else:
            print(f"{number} is an Odd number.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


def handle_menu_choice(choice: int) -> bool:
    """
    Executes the corresponding action based on the user's menu choice.
    
    Args:
        choice (int): The menu option selected by the user.
    
    Returns:
        bool: True if the program should terminate, False otherwise.
    """
    if choice == 1:
        greet_user()
        return False  # Continue the program loop
    elif choice == 2:
        even_odd_checker_action()
        return False  # Continue the program loop
    elif choice == 3:
        print("Exiting program. Goodbye!")
        return True  # Terminate the program
    else:
        print("Invalid choice. Please choose a valid option (1-3).")
        return False  # Continue the program loop


def main() -> None:
    """
    Main function to run the menu-driven program.
    Uses a loop to continuously display the menu and process user choices.
    """
    while True:
        display_menu()  # Show the menu
        try:
            choice = int(input("Enter your choice (1-3): "))  # Get user input for menu choice
            if handle_menu_choice(choice):  # If the choice leads to program exit
                break  # Exit the loop and terminate the program
        except ValueError:
            print("Invalid input. Please enter a valid number between 1 and 3.")


# Start the program
if __name__ == "__main__":
    main()
