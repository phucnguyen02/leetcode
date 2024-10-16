class Solution:
    def spiralOrder(self, matrix):
        m, n = len(matrix), len(matrix[0])
        up, down, left, right = 0, m - 1, 0, n - 1
        res = []
        while len(res) < m * n:
            for col in range(left, right + 1):
                res.append(matrix[up][col])
        
            for row in range(up + 1, down + 1):
                res.append(matrix[row][right])

            if up != down:
                for col in range(right - 1, left - 1, -1):
                    res.append(matrix[down][col])

            if left != right:
                for row in range(down - 1, up, -1):
                    res.append(matrix[row][left])

            left += 1
            right -= 1
            up += 1
            down -= 1
            
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
    print(sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))


# Traverse with borders in place. Make sure to check up != down and left != right to prevent doing it twice on the same row/column