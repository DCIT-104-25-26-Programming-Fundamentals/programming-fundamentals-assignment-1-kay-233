# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# ============================================================================def read_matrix(name="Matrix"):
    """Reads an M x N matrix from user input."""
    print(f"\n--- Enter {name} ---")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    
    matrix = []
    for i in range(rows):
        while True:
            try:
                row_input = input(f"Enter row {i + 1} (space-separated values): ")
                row = [float(x) if '.' in x else int(x) for x in row_input.split()]
                if len(row) != cols:
                    print(f"Error: Expected {cols} values, but got {len(row)}. Try again.")
                    continue
                matrix.append(row)
                break
            except ValueError:
                print("Invalid input. Please enter numbers separated by spaces.")
                
    return matrix

def print_matrix(matrix):
    """Displays a matrix in a neat grid format."""
    for row in matrix:
        print("  ".join(f"{str(val):<5}" for val in row))

def transpose_matrix(matrix):
    """Computes and returns the transpose of a given M x N matrix."""
    if not matrix or not matrix[0]:
        return []
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Create an N x M result matrix filled with zeros
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
            
    return transposed

def add_matrices(matrix_a, matrix_b):
    """Computes the element-wise sum of two matrices of the same size."""
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    
    if len(matrix_b) != rows or len(matrix_b[0]) != cols:
        raise ValueError("Matrices must have the exact same dimensions for addition.")
        
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]
            
    return result

def multiply_matrices(matrix_a, matrix_b):
    """Computes the matrix product A × B (size M x P)."""
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0])
    
    if cols_a != rows_b:
        raise ValueError("Columns of Matrix A must match Rows of Matrix B for multiplication.")
        
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
                
    return result

if __name__ == "__main__":
    print("=== Matrix Operations Program ===")
    print("1. Transpose Matrix")
    print("2. Add Two Matrices")
    print("3. Multiply Two Matrices")
    
    choice = input("\nChoose an operation (1, 2, or 3): ").strip()
    
    if choice == "1":
        mat = read_matrix("Matrix")
        print("\nOriginal Matrix:")
        print_matrix(mat)
        print("\nTransposed Matrix:")
        print_matrix(transpose_matrix(mat))
        
    elif choice == "2":
        mat_a = read_matrix("Matrix A")
        mat_b = read_matrix("Matrix B")
        try:
            res = add_matrices(mat_a, mat_b)
            print("\nResult of Addition (A + B):")
            print_matrix(res)
        except ValueError as e:
            print(f"\nError: {e}")
            
    elif choice == "3":
        mat_a = read_matrix("Matrix A")
        mat_b = read_matrix("Matrix B")
        try:
            res = multiply_matrices(mat_a, mat_b)
            print("\nResult of Multiplication (A × B):")
            print_matrix(res)
        except ValueError as e:
            print(f"\nError: {e}")
            
    else:
        print("Invalid choice. Please run the program again and select 1, 2, or 3.")
# =============================================================================

