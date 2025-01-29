def containsInRow(board, row, checkNum):
    for i in range(9):
        if board[row][i] == checkNum:
            return True
    return False

def containsInColumn(board, col, checkNum):
    for i in range(9):
        if board[i][col] == checkNum:
            return True
    return False

def containsIn3x3Box(board, row, col, checkNum):
    # Calculate the start index of the box in which we currently are
    # 0     ->      0,        0%3 = 0
    # 1     ->      0,        1%3 = 1
    # 2     ->      0,        2%3 = 2
    # 3     ->      3,        3%3 = 0
    # 4     ->      3,        4%3 = 1
    # 5     ->      3,        5%3 = 2
    # 6     ->      6,        6%3 = 0
    # 7     ->      6,        7%3 = 1
    # 8     ->      6,        8%3 = 2

    currBoxRow = row - (row % 3)
    currBoxCol = col - (col % 3)

    for r in range(3):
        for c in range(3):
            if board[currBoxRow + r][currBoxCol + c] == checkNum:
                return True
    
    return False

def isValid(board, row, col, checkNum):
    # return not(containsInRow(board, row, checkNum) or containsInColumn(board, col, checkNum) or containsIn3x3Box(board, row, col, checkNum))
    if (containsInRow(board, row, checkNum) or containsInColumn(board, col, checkNum) or containsIn3x3Box(board, row, col, checkNum)):
        return False
    else:
        return True
    


def solveSudoku(sudokuBoard):
    # Go through every cell in board
    for c in range(9):
        for r in range(9):
            # If cell is not yet solved
            if sudokuBoard[r][c] == 0:
                # Check if every number can be there placed
                for checkNum in range(1, 10):
                    if isValid(sudokuBoard, r, c, checkNum):
                        sudokuBoard[r][c] = checkNum

                        # Solve the rest of board in a recurssive way
                        if solveSudoku(sudokuBoard):
                            return True
                        
                        # Undo if sudoku not solved
                        sudokuBoard[r][c] = 0
                # Sudoku can not be solved
                return False
    # Sudoku is now solved
    return True
            

# if __name__ == "__main__":
#     mat = [
#         [3, 0, 6, 5, 0, 8, 4, 0, 0],
#         [5, 2, 0, 0, 0, 0, 0, 0, 0],
#         [0, 8, 7, 0, 0, 0, 0, 3, 1],
#         [0, 0, 3, 0, 1, 0, 0, 8, 0],
#         [9, 0, 0, 8, 6, 3, 0, 0, 5],
#         [0, 5, 0, 0, 9, 0, 6, 0, 0],
#         [1, 3, 0, 0, 0, 0, 2, 5, 0],
#         [0, 0, 0, 0, 0, 0, 0, 7, 4],
#         [0, 0, 5, 2, 0, 6, 3, 0, 0]
#         # [1, 0, 0, 0, 0, 0, 0, 0, 0],
#         # [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         # [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         # [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         # [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         # [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         # [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         # [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         # [0, 0, 0, 0, 0, 0, 0, 0, 0],

#     ]

#     solveSudoku(mat)

#     for row in mat:
#         print(" ".join(map(str, row)))
