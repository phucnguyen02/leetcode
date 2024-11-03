class Solution:
    def countBattleships(self, board) -> int:
        res = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    res += 1
                    if i >= 1 and board[i - 1][j] == "X":
                        res -= 1
                    elif j >= 1 and board[i][j - 1] == "X":
                        res -= 1

        return res
    
# Every time we see an X, increment the result. If the left or above neighbor is an X and our current cell is an X then decrement the counter to avoid duplicates.