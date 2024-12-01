def is_safe(arr, x, y, n):
    for row in range(x):  # Check if there is a queen in the same column
        if arr[row][y] == 1:
            return False
    
    row, col = x, y  # Check upper-left diagonal
    while row >= 0 and col >= 0:
        if arr[row][col] == 1:
            return False
        row -= 1
        col -= 1
    
    row, col = x, y  # Check upper-right diagonal
    while row >= 0 and col < n:
        if arr[row][col] == 1:
            return False
        row -= 1
        col += 1  # If no conflicts, it's safe to place a queen at position (x, y)
    
    return True

def n_queen(arr, x, n):
    if x >= n:  # If all queens are placed successfully, return True
        return True
    
    for col in range(n):  # Try placing the queen in each column of the current row
        if is_safe(arr, x, col, n):
            arr[x][col] = 1  # Recur to place the remaining queens
            
            if n_queen(arr, x + 1, n):
                return True  # If placing the queen here doesn't lead to a solution, backtrack
            
            arr[x][col] = 0
    
    return False  # If no column is safe in this row, return False

#---------------------------------------------------------------
n = int(input("Enter number of Queens: "))

arr = [[0] * n for i in range(n)]  # Initialize the chessboard

if n_queen(arr, 0, n):  # Try to place queens on the chessboard
    for row in arr:  # Print the chessboard if a solution is found
        for item in row:
            print(item, end=" ")
        print()
else:
    print("Solution does not exist.")
