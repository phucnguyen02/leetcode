DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        def bfs(r, c):
            visited = set((r, c))
            queue = [(r, c, 0)]
            while queue:
                cur_r, cur_c, dist = queue.pop(0)

                for dr, dc in DIRECTIONS:
                    new_r = cur_r + dr
                    new_c = cur_c + dc
                    
                    if not (0 <= new_r < len(rooms) and 0 <= new_c < len(rooms[0])):
                        continue

                    if (new_r, new_c) in visited:
                        continue

                    if rooms[new_r][new_c] == -1:
                        continue
                    
                    if dist + 1 > rooms[new_r][new_c]:
                        continue

                    visited.add((new_r, new_c))
                    rooms[new_r][new_c] = dist + 1
                    queue.append((new_r, new_c, dist + 1))
            
        m, n = len(rooms), len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    bfs(i, j)

# BFS on the gates. Only visit empty cells if the current distance is smaller to save time
