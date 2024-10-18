class Solution:
    def findDiagonalOrder(self, nums):
        queue = []
        queue.append((0, 0))
        visited = set((0, 0))
        res = []
        while queue:
            r, c = queue.pop(0)
            res.append(nums[r][c])

            for dr, dc in [(1,0), (0, 1)]:
                new_r = r + dr
                new_c = c + dc

                if new_r < len(nums) and new_c < len(nums[new_r]) and (new_r, new_c) not in visited:
                    visited.add((new_r, new_c))
                    queue.append((new_r, new_c))

        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
    print(sol.findDiagonalOrder([[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]))


# Do BFS traversal but add the cell below before adding the cell to the right.