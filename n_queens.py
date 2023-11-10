from math import *

class Solution:
    def n_queens(self, n):
        if not n: return []
        if n == 1: return [['Q']]
        res = []
        board = ['.'*n for i in range(n)]
        col = [False]*n
        diag1 = [False]*(2*n)
        diag2 = [False]*(2*n)
        def backtracking(r):
            if r == n:
                res.append(board[:][:])
                return
            for c in range(n):
                if col[c] or diag1[r + c] or diag2[r-c+n-1]: continue
                col[c] = diag1[r+c] = diag2[r-c+n-1] = True
                cur_row = list(board[r])
                cur_row[c] = 'Q'
                board[r] = ''.join(cur_row)
                backtracking(r + 1)
                cur_row[c] = '.'
                board[r] = ''.join(cur_row)
                col[c] = diag1[r+c] = diag2[r-c+n-1] = False
        backtracking(0)
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.n_queens(0))
    print(sol.n_queens(1))
    print(sol.n_queens(3))
    print(sol.n_queens(4))
    print(sol.n_queens(5))

# Attempt to place a queen in the first row, see if you can place queens in other rows based on that data
# Checks for valid position with a column array and 2 diagonal arrays.
# If a queen occupies a position, that column and corresponding diagonals are also marked as occupied.
# A solution is valid if n queens are placed into n rows

# res = []
# col = [False]*n
# diag1 = [False]*(2*n)
# diag2 = [False]*(2*n)
# backtrack(r):
#   if r == n:
#       append board into res
#       return
#   for c = 0, ..., n-1
#       if board[r][c] is not valid then continue
#       col[c] = diag1[r + c] = diag2[r - c + n - 1] = True
#       board[r][c] = 'Q'
#       backtrack(r + 1)
#       board[r][c] = '.'
#       col[c] = diag1[r + c] = diag2[r - c + n - 1] = True
#
# backtrack(0) 
# return res