# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
def generate_fibonacci(n):
    """Generates a list containing the first n terms of the Fibonacci sequence."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
        
    fib_sequence = [0, 1]
    for _ in range(2, n):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
        
    return fib_sequence

def is_fibonacci(number):
    """Determines whether a given number belongs to the Fibonacci sequence."""
    if number < 0:
        return False
        
    a, b = 0, 1
    while a < number:
        a, b = b, a + b
        
    return a == number

if __name__ == "__main__":
    print("=== Fibonacci Sequence Program ===")
    print("1. Print the first N terms")
    print("2. Check if a number is in the Fibonacci sequence")
    
    choice = input("\nChoose an option (1 or 2): ").strip()
    
    if choice == "1":
        try:
            n = int(input("How many terms? "))
            if n <= 0:
                print("Error: Please enter a positive integer greater than 0.")
            else:
                seq = generate_fibonacci(n)
                print("Fibonacci sequence:", " ".join(map(str, seq)))
        except ValueError:
            print("Please enter a valid whole number.")
            
    elif choice == "2":
        try:
            num = int(input("Enter a number to check: "))
            if is_fibonacci(num):
                print(f"{num} is a Fibonacci number.")
            else:
                print(f"{num} is NOT a Fibonacci number.")
        except ValueError:
            print("Please enter a valid whole number.")
            
    else:
        print("Invalid choice. Please run the program again and select 1 or 2.
              

