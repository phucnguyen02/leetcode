class Solution:
    def valid(self, r, c, m, n):
        return 0 <= r < m and 0 <= c < n
    
    def findDiagonalOrder(self, mat):
        cur_r, cur_c = 0, 0
        m, n = len(mat), len(mat[0])
        dir = (-1, 1)
        res = []
        traversed = 0
        while traversed != m * n:
            res.append(mat[cur_r][cur_c])
            if not self.valid(cur_r + dir[0], cur_c + dir[1], m, n):
                if dir == (-1, 1):
                    if cur_c == n - 1:
                        cur_r += 1
                    else:
                        cur_c += 1
                else:
                    if cur_r == m - 1:
                        cur_c += 1
                    else:
                        cur_r += 1
                dir = (-1, 1) if dir == (1, -1) else (1, -1)
            else:
                cur_r += dir[0]
                cur_c += dir[1]
            traversed += 1
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
    print(sol.findDiagonalOrder([[1,2],[3,4]]))

# We're always only going in 2 directions: up right (-1, 1) and down left (1, -1).
# If we can no longer go up right, we move to the right cell unless we can't anymore, then we move downward instead.
# If we can no longer go down left, we move to the downward cell unless we can't anymore, then we move right instead.
# Keep going until we've traversed every cell in the matrix


