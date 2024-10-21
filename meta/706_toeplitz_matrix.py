class Solution:
    def isToeplitzMatrix(self, matrix) -> bool:
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] != matrix[i-1][j-1]: return False
        return True
    
# Check whether every cell is equal to its top left neighbor