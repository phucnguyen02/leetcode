class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int):
        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        traversed = []

        step = 1
        direction = 0
        while len(traversed) < rows * cols:
            # direction = 0 -> East, direction = 1 -> South
            # direction = 2 -> West, direction = 3 -> North
            for _ in range(2):
                for _ in range(step):
                    if 0 <= rStart < rows and 0 <= cStart < cols:
                        traversed.append([rStart, cStart])
                    rStart += dir[direction][0]
                    cStart += dir[direction][1]

                direction = (direction + 1) % 4
            step += 1
        return traversed
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.spiralMatrixIII(1, 4, 0, 0))
    print(sol.spiralMatrixIII(5, 6, 1, 4))

# Each step of the way, we got east and south step number of steps, then increment step, then go west and north that amount, increment again, then repeat with east and south
# We can step out of the matrix, but only add cells to the result that are within the matrix