class Solution:
    def sequence_2d_array(self, arr, sequence):
        m = len(arr)
        n = len(arr[0])
        l = len(sequence)
        dp = [[False for i in range(l)] for j in range(n*m)]
        for i in range(m):
            for j in range(n):
                idx = i * n + j
                if sequence[0] == arr[i][j]:
                    dp[idx][0] = True

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for k in range(1, l):
            for r in range(m):
                for c in range(n):
                    idx = r * n + c
                    for (dr, dc) in directions:
                        new_r = r + dr
                        new_c = c + dc
                        if 0 <= new_r < m and 0 <= new_c < n:
                            new_idx = new_r * n + new_c
                            dp[idx][k] = sequence[k] == arr[r][c] and (dp[idx][k] or dp[new_idx][k - 1])
        
        # for (i, row) in enumerate(dp):
        #     print(i, row)

        for i in range(n*m):
            if dp[i][-1] == True: return True

        return False

        

if __name__ == "__main__":
    sol = Solution()
    print(sol.sequence_2d_array([[1, 2, 3], [3, 4, 5], [5, 6, 7]], [1, 3, 4, 6]))
    print(sol.sequence_2d_array([[1, 2, 3], [3, 4, 5], [5, 6, 7]], [1, 3, 4, 7]))


# Variables: dp(i, j) with i being the index based on the row and column (2d array is flattened) and j being the index of the sequence. 
# dp(i, j) whether you can create the sequence up to index j if the sequence ends at the corresponding index i from the array
    
# Base case: dp(i, 0) = True if arr[i] == sequence[0] and False otherwise

# Recurrence relation:
# dp(i, j) = (sequence[j] == arr[i]) and (dp(i, j) or dp(k, j - 1)) with k being all the neighbors of i

# Return true if the last column has a true, and false otherwise
    
# For any row or column, provided the value at that position is equal to the current sequence element, it is possible to recreate the entire sequence
# provided one of its neighbors is equal to the preceding sequence element.
    
