import random  # Import the random module for generating CPU's choice.

# Dictionary to store ASCII art for Rock, Paper, and Scissors.
art_ascii = {
    'Rock': """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    'Paper': """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""",
    'Scissors': """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
}

# Loop until valid input is received from the user.
while True:
    user_choice = input("Welcome to Rock, Paper, and Scissor.\nLet's Play.\nPick 0 for Rock,\nPick 1 for Paper,\nPick 2 for Scissors.\nWhat Would you Choose?: ")
    if user_choice.isdigit() and int(user_choice) in [0, 1, 2]:
        user_choice = int(user_choice)  # Convert user input to integer.
        break  # Exit loop if input is valid.
    else:
        print("Invalid input. Please enter 0, 1, or 2.")  # Prompt for valid input.

# Generate CPU's choice randomly.
cpu_choice = random.randint(0, 2)

# Determine the winner based on user and CPU choices.
if user_choice == cpu_choice:
    # Display ASCII art for user's choice.
    print(art_ascii[list(art_ascii.keys())[user_choice]])
    print(f"^The user has chosen {list(art_ascii.keys())[user_choice]}") 
    # Display ASCII art for CPU's choice.
    print(art_ascii[list(art_ascii.keys())[cpu_choice]])
    print(f"^The CPU has chosen {list(art_ascii.keys())[cpu_choice]}")
    print("It's a Draw")  # Declare a draw.
elif (user_choice == 0 and cpu_choice == 2) or \
     (user_choice == 1 and cpu_choice == 0) or \
     (user_choice == 2 and cpu_choice == 1):
    # Display ASCII art for user's choice.
    print(art_ascii[list(art_ascii.keys())[user_choice]])
    print(f"^The user has chosen {list(art_ascii.keys())[user_choice]}")
    # Display ASCII art for CPU's choice.
    print(art_ascii[list(art_ascii.keys())[cpu_choice]])
    print(f"^The CPU has chosen {list(art_ascii.keys())[cpu_choice]}")
    print("You won!")  # Declare user as winner.
else:
    # Display ASCII art for user's choice.
    print(art_ascii[list(art_ascii.keys())[user_choice]])
    print(f"^The user has chosen {list(art_ascii.keys())[user_choice]}")
    # Display ASCII art for CPU's choice.
    print(art_ascii[list(art_ascii.keys())[cpu_choice]])
    print(f"^The CPU has chosen {list(art_ascii.keys())[cpu_choice]}")
    print("You lost")  # Declare CPU as winner.
