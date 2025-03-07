def display_menu() -> None:
    """
    Displays the menu options to the user.
    """
    print("\nMenu:")
    print("1. Greet User")
    print("2. Check Even/Odd")
    print("3. Exit")


def greet_user() -> None:
    """
    Prints a greeting message to the user.
    """
    print("Hello! Welcome!")


def even_odd_checker_action() -> None:
    """
    Prompts the user to enter an integer and checks if it is even or odd.
    """
    try:
        num = int(input("Enter an integer: "))
        if num % 2 == 0:
            print(f"{num} is an Even number.")
        else:
            print(f"{num} is an Odd number.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")


def handle_menu_choice(choice: int) -> bool:
    """
    Executes the corresponding action based on the user's menu choice.
    
    Parameters:
    choice (int): The user's menu option (1, 2, or 3).
    
    Returns:
    bool: True to exit the program, False to continue.
    """
    if choice == 1:
        greet_user()
    elif choice == 2:
        even_odd_checker_action()
    elif choice == 3:
        print("Exiting program. Goodbye!")
        return True  # Signal to exit the loop
    else:
        print("Invalid choice, please try again.")
    return False  # Continue the loop


def main() -> None:
    """
    Main function to drive the menu-driven program.
    Continuously displays the menu and processes user choices.
    """
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-3): "))
            if handle_menu_choice(choice):
                break
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 3.")


if __name__ == "__main__":
    main()
