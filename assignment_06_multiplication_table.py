# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
def print_single_table(number):
    """Prints the multiplication table for a single number from 1 to 12."""
    print(f"\nMultiplication Table for {number}:")
    for i in range(1, 13):
        result = number * i
        print(f"{number}  x  {i:<2} =  {result}")

def print_tables_up_to_n(n):
    """Prints multiplication tables from 1 up to N, with a separator in between."""
    if n <= 0:
        print("Error: Please enter a positive integer greater than 0.")
        return
        
    for current in range(1, n + 1):
        print_single_table(current)
        if current < n:
            print("-" * 27)

if __name__ == "__main__":
    print("=== Multiplication Table Generator ===")
    print("1. Print a single multiplication table")
    print("2. Print tables from 1 to N")
    
    choice = input("\nChoose an option (1 or 2): ").strip()
    
    if choice == "1":
        try:
            num = int(input("Enter a number: "))
            print_single_table(num)
        except ValueError:
            print("Please enter a valid whole number.")
            
    elif choice == "2":
        try:
            n = int(input("Enter N (positive integer): "))
            if n <= 0:
                print("Error: N must be a positive integer greater than 0.")
            else:
                print_tables_up_to_n(n)
        except ValueError:
            print("Please enter a valid whole number.")
            
    else:
        print("Invalid choice. Please run the program again and select 1 or 2.")
# =============================================================================

