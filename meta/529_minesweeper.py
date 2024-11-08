DIRECTIONS = [(0, 1), (0, -1), (1, 1), (1, -1), (1, 0), (-1, 1), (-1, 0), (-1, -1)]

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def dfs(r, c):
            mine_count = 0
            for dr, dc in DIRECTIONS:
                new_r = r + dr
                new_c = c+ dc
                if not (0 <= new_r < len(board) and 0 <= new_c < len(board[0])):
                    continue

                if board[new_r][new_c] == "M":
                    mine_count += 1

            if mine_count:
                board[r][c] = str(mine_count)
                return
            
            board[r][c] = "B"
            for dr, dc in DIRECTIONS:
                new_r = r + dr
                new_c = c+ dc
                if not (0 <= new_r < len(board) and 0 <= new_c < len(board[0])):
                    continue
                
                if board[new_r][new_c] != "E":
                    continue

                dfs(new_r, new_c)

            
        r, c = click
        if board[r][c] == "M":
            board[r][c] = "X"
        else:
            dfs(r, c)
        return board