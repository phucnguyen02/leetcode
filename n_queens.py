from math import *

class Solution:
    def n_queens(self, n):
        res = []
        board = ['.'*n for i in range(n)]
        col = [False]*n
        diag1 = [False]*(n ** 2)
        diag2 = [False]*(n ** 2)
        def backtracking(r):
            if r == n:
                res.append(board[:][:])
                return
            for c in range(n):
                #print(r, c, diag1, diag2)
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
    print(sol.n_queens(3))
    print(sol.n_queens(4))

#Preorder traversal = check left branch -> check right branch -> check current node val