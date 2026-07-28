# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
def calculate_sum(numbers):
    """Calculates the sum of a list of numbers without using sum()."""
    total = 0
    for num in numbers:
        total += num
    return total

def calculate_average(numbers):
    """Calculates the average of a list of numbers."""
    if not numbers:
        return 0
    return calculate_sum(numbers) / len(numbers)

def find_maximum(numbers):
    """Finds the maximum value in a list without using max()."""
    if not numbers:
        return None
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val

def find_minimum(numbers):
    """Finds the minimum value in a list without using min()."""
    if not numbers:
        return None
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == "__main__":
    try:
        n = int(input("How many numbers? "))
        
        if n <= 0:
            print("Error: Please enter a positive integer greater than 0.")
        else:
            numbers = []
            for i in range(1, n + 1):
                num = float(input(f"Enter number {i}: "))
                # Convert to int if it's a whole number for cleaner display
                if num.is_integer():
                    num = int(num)
                numbers.append(num)
                
            print("\nResults:")
            print(f"Sum:     {calculate_sum(numbers)}")
            print(f"Average: {calculate_average(numbers)}")
            print(f"Maximum: {find_maximum(numbers)}")
            print(f"Minimum: {find_minimum(numbers)}")
            
    except ValueError:
        print("Please enter a valid whole number for the count.")
# =============================================================================

