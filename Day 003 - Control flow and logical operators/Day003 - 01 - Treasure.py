# Display welcome message
print("Welcome to the Reasure Island.\nYour mission is to find the treasure.")

# Ask the user to choose a direction
left_or_right = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right' :")

# Check if the user chose left
if left_or_right == "left":
    # Ask the user to choose whether to swim or wait
    swim_or_wait = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. :")
    # Check if the user chose to wait
    if swim_or_wait == "wait":
        # Ask the user to choose a door color
        which_door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? :")
        # Check if the user chose the yellow door
        if which_door == "yellow":
            print("You found the treasure! You Win!")  # Winning message
        # Check if the user chose the red door
        elif which_door == "red":
            print("It's a room full of fire. Game Over.")  # Game over message
        # Check if the user chose the blue door
        elif which_door == "blue":
            print("You enter a room of beasts. Game Over.")  # Game over message
    # If the user chose to swim
    else:
        print("You get attacked by an angry trout. Game Over.")  # Game over message
# If the user chose right
else:
    print("You fell into a hole. Game Over.")  # Game over message
# End of the game