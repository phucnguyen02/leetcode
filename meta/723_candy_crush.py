class Solution:
    def candyCrush(self, board):
        m = len(board)
        n = len(board[0])
        def verify():
            nonlocal m, n
            flag = False
            for i in range(m):
                for j in range(n):
                    if board[i][j] != 0:
                        neg_cell = -abs(board[i][j])
                        if 0 < i < m - 1 and abs(board[i][j]) == abs(board[i - 1][j]) == abs(board[i + 1][j]):
                            board[i][j] = board[i - 1][j] = board[i + 1][j] = neg_cell
                            flag = True

                        if 0 < j < n - 1 and abs(board[i][j]) == abs(board[i][j - 1]) == abs(board[i][j + 1]):
                            board[i][j] = board[i][j - 1] = board[i][j + 1] = neg_cell
                            flag = True
            
            return flag
        
        def crush():
            nonlocal m, n
            for i in range(m):
                for j in range(n):
                    if board[i][j] < 0:
                        board[i][j] = 0

            
            for i in range(n):
                ptr1 = m - 1
                for j in range(m - 1, -1, -1):
                    if board[j][i] != 0:
                        board[j][i], board[ptr1][i] = board[ptr1][i], board[j][i]
                        ptr1 -= 1
            
            
        flag = verify()
        while flag:
            crush()
            flag = verify()

        return board
if __name__ == "__main__":
    sol = Solution()
    print(sol.candyCrush([[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]))
                
# Crush candies by marking ones with same adjacent absolute neighbors as negative first, then 0
# Do 2 pointers on each column from bottom to top to move all the 0s up