from collections import deque

DIRECTIONS = {"R": (0, 1), "D": (1, 0), "U": (-1, 0), "L": (0, -1)}

class Solution:
    def hasPath(self, maze, start, destination) -> bool:
        if start == destination: return True
        m, n= len(maze), len(maze[0])

        queue = deque([(start[0], start[1])])

        visited = set()
        visited.add((start[0], start[1]))

        while queue:
            r, c = queue.popleft()
            if [r, c] == destination:
                return True
            
            for dir in DIRECTIONS:
                dr, dc = DIRECTIONS[dir]
                new_r = r
                new_c = c
                while 0 <= new_r + dr < m and 0 <= new_c + dc < n and maze[new_r + dr][new_c + dc] != 1:
                    new_r += dr
                    new_c += dc

                if (new_r, new_c) in visited:
                    continue

                visited.add((new_r, new_c))
                queue.append((new_r, new_c))

        return False
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.hasPath([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], [0, 4], [4, 4]))
    print(sol.hasPath([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], [0, 4], [3, 2]))