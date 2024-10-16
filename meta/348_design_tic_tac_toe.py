from collections import defaultdict

class TicTacToe:
    def __init__(self, n: int):
        self.anti_diag_coords = set()
        for i in range(n):
            self.anti_diag_coords.add((i, n - 1 - i))

        self.rows = defaultdict(int)
        self.cols = defaultdict(int)
        self.diag = 0
        self.anti_diag = 0
        self.win = n 

    def move(self, row: int, col: int, player: int) -> int:
        score = 1 if player == 1 else -1
        if row == col: self.diag += score
        if (row, col) in self.anti_diag_coords: self.anti_diag += score
        self.rows[row] += score
        self.cols[col] += score
        if self.rows[row] == score * self.win or self.cols[col] == score*self.win or \
        self.diag == self.win * score or self.anti_diag == self.win * score:
            return 1 if score == 1 else 2
        return 0
    
# Instead of storing a matrix and updating it with O(n^2), we store 2 hash tables + 2 counters to update the game state in O(1).
# We have 2 hash tables for rows and columns and 2 counters for the diagonal and anti-diagonal.
# Every time a player makes a move, the tally for the row/column/diagonal/anti-diagonal it's in increases by 1 if it's player 1 or -1 if it's player 2.
# The game ends when the tally for any of this is equal to n or -n.