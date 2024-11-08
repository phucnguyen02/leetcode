from collections import deque

dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
class Solution:
    def shortestDistance(self, grid) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        total_sum = [[0] * cols for _ in range(rows)]
        
        def bfs(row, col, curr_count):
            min_distance = 1e9
            queue = deque()
            queue.append([row, col, 0])
            while queue:
                curr_row, curr_col, curr_step = queue.popleft()
                for dr, dc in dirs:
                    next_row = curr_row + dr
                    next_col = curr_col + dc
                    
                    if not (0 <= next_row < rows and 0 <= next_col < cols):
                        continue
                    if grid[next_row][next_col] != -curr_count:
                        continue

                    total_sum[next_row][next_col] += curr_step + 1
                    min_distance = min(min_distance, total_sum[next_row][next_col])
                    grid[next_row][next_col] -= 1
                    queue.append([next_row, next_col, curr_step + 1])
            return min_distance
                
        count = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    min_distance = bfs(row, col, count)
                    count += 1
                    if min_distance == 1e9:
                        return -1
        
        return min_distance
    
# During the first BFS we can change the visited empty land values from 0 to -1. Then during the next BFS we will only visit empty lands with a value of -1s (meaning they can 
# reach the first house), then change -1 to -2 and then perform the next BFS only on -2s, and so on...

# This approach allows us to avoid visiting any cell that cannot reach all houses.

# Can we also use this decrement in empty land value to denote that the cell has been visited?

# Imagine we are currently at cell (2, 3) with value -1 and we change its value to -2.
# In the queue the next element is (2, 4), its value is also -1 and we change its value to -2. While exploring paths from (2, 4), we see that the cell (2, 3) is adjacent, and has the value -2. However, currently, we are checking for -1 valued cells only. Hence, (2, 3) will not be inserted again in the queue, so this decrease in value can be used as a visited cell check because when a cell has been visited, then its value will be 1 less and it will not satisfy the condition to be inserted in the queue.

# If there was an empty land cell that was not reachable in the previous iteration, then its value has not been decreased, hence we will not insert that cell in the queue when we start a BFS from another house cell.
# Therefore, this approach prunes many iterations and saves some time since we are not creating a new matrix to track visited cells for each BFS call.

