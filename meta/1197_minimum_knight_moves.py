class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        queue = [(0, 0, 0)]
        directions = [(1, 2), (2, 1), (2, -1), (1, -2),
                   (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        visited = set()
        visited.add((0, 0))
        while True:
            r, c, dist = queue.pop(0)

            if r == x and c == y:
                return dist

            for dr, dc in directions:
                new_r = r + dr
                new_c = c + dc

                if (new_r, new_c) in visited:
                    continue

                visited.add((new_r, new_c))
                queue.append((new_r, new_c, dist + 1))

# BFS on the knight