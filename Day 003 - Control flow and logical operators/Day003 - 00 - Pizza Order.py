# Greet the customer
print("Welcome to the Python Pizza Deliveries")

# Get pizza size input and convert it to uppercase
size = input("What size pizza do you want? S, M, or L :").upper()

# Ask if customer wants pepperoni and convert input to uppercase
add_pepperoni = input("Do you want to add pepperoni? Y or N :").upper()

# Ask if customer wants extra cheese and convert input to uppercase
extra_cheese = input("Do you want to add extra cheese? Y or N :").upper()

# Initialize the bill
bill = 0

# Calculate the cost based on size
if size == "S":
    bill += 15  # Base price for small pizza
    if add_pepperoni == "Y":
        bill += 2  # Additional cost for pepperoni on small pizza
elif size == "M":
    bill += 20  # Base price for medium pizza
    if add_pepperoni == "Y":
        bill += 3  # Additional cost for pepperoni on medium/large pizza
elif size == "L":
    bill += 25  # Base price for large pizza
    if add_pepperoni == "Y":
        bill += 3  # Additional cost for pepperoni on medium/large pizza

# Add cost of extra cheese if requested
if extra_cheese == "Y":
    bill += 1

# Print the final bill
print(f"Your final bill is: ${bill}")
