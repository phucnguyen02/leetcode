from collections import Counter

class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def backtracking(r, c):
            if c == 9:
                r += 1
                c = 0

            if r == 9:
                return True
            
            if board[r][c] != ".":
                return backtracking(r, c + 1)
            
            for ch in "123456789":
                if not valid(r, c, ch):
                    continue

                board[r][c] = ch
                if backtracking(r, c + 1):
                    return True
                board[r][c] = "."
            
            return False

        def valid(r, c, val):
            count_row = Counter(board[r])
            if val in count_row: return False
            column = [board[i][c] for i in range(9)]
            count_col = Counter(column)
            if val in count_col: return False

            start_row = 3 * (r // 3)
            start_col = 3 * (c // 3)

            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == val: return False
            
            return True

        backtracking(0, 0)


# Do backtracking on every "." cell of the grid. Check every value from "123456789", as long as it's valid.
# We check whether a value is valid in a cell by checking its column, row, and subgrid. To get the subgrid for a current cell,
# find the top left cell of the grid with the formula (3 * (r//3), 3 * (c // 3))
# If it's valid, we go to the next cell (column + 1). If column == 9 then we go to the next row. If we've gone through all 9 rows
# then all of our values are valid, so we return true