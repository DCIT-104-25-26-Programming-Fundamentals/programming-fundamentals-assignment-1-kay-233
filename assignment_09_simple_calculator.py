# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference between two numbers."""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide(a, b):
    """Returns the division of two numbers rounded to 2 decimal places."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return round(a / b, 2)

def modulus(a, b):
    """Returns the remainder of division between two numbers."""
    if b == 0:
        raise ValueError("Cannot perform modulus by zero.")
    return a % b

def exponentiate(a, b):
    """Returns the result of raising the first number to the power of the second."""
    return a ** b

def format_number(n):
    """Formats a number to remove decimal places if it's a whole number."""
    if isinstance(n, float) and n.is_integer():
        return int(n)
    return n

def main():
    """Main program loop for the simple calculator application."""
    while True:
        print("\n============================")
        print("       SIMPLE CALCULATOR")
        print("============================")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Exponentiation")
        print("7. Quit")
        
        choice = input("Select an operation (1-7): ").strip()
        
        if choice == "7":
            print("Goodbye!")
            break
            
        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Error: Invalid choice. Please enter a number between 1 and 7.")
            continue
            
        try:
            num1 = float(input("Enter first number : "))
            num2 = float(input("Enter second number: "))
            
            # Format inputs for cleaner output display if they are whole numbers
            f_num1 = format_number(num1)
            f_num2 = format_number(num2)
            
            if choice == "1":
                res = format_number(add(num1, num2))
                print(f"Result: {f_num1} + {f_num2} = {res}")
            elif choice == "2":
                res = format_number(subtract(num1, num2))
                print(f"Result: {f_num1} - {f_num2} = {res}")
            elif choice == "3":
                res = format_number(multiply(num1, num2))
                print(f"Result: {f_num1} * {f_num2} = {res}")
            elif choice == "4":
                res = divide(num1, num2)
                # Keep 2 decimal places for division as per specifications
                print(f"Result: {f_num1} / {f_num2} = {res}")
            elif choice == "5":
                res = format_number(modulus(num1, num2))
                print(f"Result: {f_num1} % {f_num2} = {res}")
            elif choice == "6":
                res = format_number(exponentiate(num1, num2))
                print(f"Result: {f_num1} ** {f_num2} = {res}")
                
        except ValueError as e:
            if "Cannot" in str(e):
                print(f"Error: {e}")
            else:
                print("Error: Please enter valid numeric values.")

if __name__ == "__main__":
    main()
# =============================================================================

