DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    def exist(self, board, word: str) -> bool:
        m = len(board)
        n = len(board[0])
        def dfs(r, c, idx):
            if idx == len(word):
                return True
    
            ch = board[r][c]
            board[r][c] = "!"
            for dr, dc in DIRECTIONS:
                new_r = r + dr
                new_c = c + dc

                if not (0 <= new_r < len(board) and 0 <= new_c < len(board[0])):
                    continue

                
                if board[new_r][new_c] == word[idx]:
                    if dfs(new_r, new_c, idx + 1):
                        return True
            board[r][c] = ch
            return False
            
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 1): return True

        return False
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
    print(sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
    print(sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
    print(sol.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS"))

# Do backtracking starting from the first character of the word. Only traverse to neighbors that's equal to the next index of the word
# Change the current square to an invalid character so we don't have to visit it again, and change it back to normal after we're done traversing its neighbors,
# so that others will have an accurate value