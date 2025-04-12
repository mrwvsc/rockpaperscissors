import random  # Importing the random module for generating computer choices
from time import sleep  # Importing sleep to add delays for better user experience

def get_user_input():

    # Gets user input for the desired option and ensures valid input.
    # Displays the menu and prompts the user to select Rock, Paper, Scissors, or Exit.
    # Returns:
    #   int: The user's choice (1 for Rock, 2 for Paper, 3 for Scissors, 4 for Exit).
    
    while True:
        print("\nWelcome to Rock-Paper-Scissors! You will play against the computer.")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Exit\n")
        
        try:
            # Prompt the user for their choice
            choice = int(input("Enter the number of your choice: "))
            if choice in [1, 2, 3, 4]:  # Validate the choice
                sleep(1)  # Add a delay for better user experience
                return choice
            else:
                print("Invalid choice. Please select a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_computer_choice():
    # Randomly generates the computer's choice.
    # Returns:
    #    int: The computer's choice (1 for Rock, 2 for Paper, 3 for Scissors).
    return random.randint(1, 3)

def determine_winner(user_choice, computer_choice):
    """
    Determines the winner of the game based on the user's and computer's choices.
    Prints the result of the game.
    Args:
        user_choice (int): The user's choice (1 for Rock, 2 for Paper, 3 for Scissors).
        computer_choice (int): The computer's choice (1 for Rock, 2 for Paper, 3 for Scissors).
    """
    options = {1: "Rock", 2: "Paper", 3: "Scissors"}  # Mapping choices to their names
    print(f"\nYou chose {options[user_choice]}.")
    sleep(1)
    print(f"Computer chose {options[computer_choice]}.")
    sleep(1)
    
    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        print("You win!")
    else:
        print("Computer wins!")

def play_game():
    # Main game loop for Rock-Paper-Scissors.
    # Continuously prompts the user to play until they choose to exit.
    while True:
        user_choice = get_user_input()  # Get the user's choice
        if user_choice == 4:  # Exit the game if the user chooses 4
            sleep(1)
            print("Thanks for playing! Goodbye.")
            break
        
        computer_choice = get_computer_choice()  # Get the computer's choice
        sleep(1)
        determine_winner(user_choice, computer_choice)  # Determine and display the winner

# Entry point of the program
if __name__ == "__main__":
    play_game()
