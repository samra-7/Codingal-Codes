# Sum of n natural numbers

# Input from user
n = int(input("Enter a positive integer: "))

# Check for valid input
if n < 1:
    print("Please enter a number greater than 0.")
else:
    # Using formula: sum = n * (n + 1) // 2
    total = n * (n + 1) // 2
    print(f"Sum of first {n} natural numbers is: {total}")
