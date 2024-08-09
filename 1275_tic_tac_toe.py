from collections import defaultdict, Counter

class Solution:
    def validate_count(self, count):
        for key in count:
            if count[key] == 3 and key != " ":
                return key
        
        return None

    def check_row(self, board):
        for row in board:
            count = Counter(row)
            if self.validate_count(count): return self.validate_count(count)
        
        return None
    
    def check_column(self, board):
        for i in range(3):
            column = [board[j][i] for j in range(3)]
            count = Counter(column)
            if self.validate_count(count): return self.validate_count(count)

        return None
    
    def check_diag(self, board):
        count = defaultdict(int)
        for i in range(3):
            count[board[i][i]] += 1
            
        if self.validate_count(count): return self.validate_count(count)

        count = defaultdict(int)
        for i in range(3):
            count[board[i][3-i-1]] += 1
            
        if self.validate_count(count): return self.validate_count(count)
                
        return None
    
    def tictactoe(self, moves) -> str:
        board = [[' ' for i in range(3)] for j in range(3)]
        turn = 1
        for move in moves:
            move_r, move_c = move
            board[move_r][move_c] = "A" if turn == 1 else "B"
            turn *= -1
        
        if self.check_row(board): return self.check_row(board)

        if self.check_column(board): return self.check_column(board)

        if self.check_diag(board): return self.check_diag(board)

        return "Draw" if len(moves) == 9 else "Pending"
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]]))
    print(sol.tictactoe([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]))
    print(sol.tictactoe([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]))

# Check every column, row and diagonal to see if the counts of a non-empty character is 3