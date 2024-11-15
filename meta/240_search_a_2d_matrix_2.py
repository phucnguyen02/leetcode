class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        row = 0
        col = n - 1
        while row < m and col >= 0:
            if matrix[row][col] > target:
                col -= 1
            elif matrix[row][col] < target:
                row += 1
            else:
                return True
        return False
    
# Initialize a pointer at the top right. If the number is less than target, move down. Larger, move left.
# If it's larger than the target then we know every number in the part of the column below it is larger than the target, so we don't need to consider that part of the column
# Similarly, if it's smaller than the target then every number before it in the row is smaller than the target, so we don't need to consider that part either