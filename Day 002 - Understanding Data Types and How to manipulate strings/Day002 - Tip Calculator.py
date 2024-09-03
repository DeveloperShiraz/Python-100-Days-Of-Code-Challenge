# Greet the user
print("Welcome to the tip calculator!")

# Ask for the total bill amount
total_bill = input("What was the total bill? $")

# Ask for the desired tip percentage
total_percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")

# Ask for the number of people splitting the bill
number_of_people = input("How many people to split the bill? ")

# Calculate the amount each person should pay
each_person = float(int(total_bill) + (int(total_percentage) / 100) * 100) / int(number_of_people)

# Print the result
print(f"Each person should pay: ${each_person}\nThank you for using the tip calculator!")