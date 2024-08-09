from collections import defaultdict, Counter

class Solution:
    def validate_count(self, count):
        for key in count:
            if count[key] > 1 and key != ".":
                return False
        
        return True
    
    def check_row(self, board):
        for row in board:
            count = Counter(row)
            if not self.validate_count(count): return False
        
        return True
    
    def check_column(self, board):
        for i in range(9):
            column = [board[j][i] for j in range(9)]
            count = Counter(column)
            if not self.validate_count(count): return False

        return True
    
    def check_subbox(self, board):
        for box in [(0, 0), (3, 0), (6, 0), (0, 3), (3, 3), (6, 3), (0, 6), (3, 6), (6, 6)]:
            box_r, box_c = box
            count = defaultdict(int)
            for i in range(3):
                for j in range(3):
                    count[board[box_r + i][box_c + j]] += 1
            
            if not self.validate_count(count): return False
                
        return True

    def isValidSudoku(self, board) -> bool:
        return self.check_row(board) and self.check_column(board) and self.check_subbox(board)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
    print(sol.isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
    
# Check every column, row and subbox to see if the counts of the digits are valid