import heapq

class Solution:
    def kthSmallest2(self, matrix, k: int) -> int:
        n = len(matrix)
        heap = []
        for i in range(n):
            for j in range(n):
                if len(heap) < k:
                    heapq.heappush(heap, -matrix[i][j])
                else:
                    if -heap[0] > matrix[i][j]:
                        heapq.heappop(heap)
                        heapq.heappush(heap, -matrix[i][j])
        return -heap[0]
    
    def count_smaller(self, matrix, mid, smaller, larger):
        count = 0
        row = len(matrix) - 1
        col = 0

        while row >= 0 and col < len(matrix[0]):
            if matrix[row][col] > mid:
                larger = min(larger, matrix[row][col])
                row -= 1
            else:
                count += row + 1
                smaller = max(smaller, matrix[row][col])
                col += 1
        
        return count, smaller, larger

    def kthSmallest(self, matrix, k: int) -> int:
        left = matrix[0][0]
        right = matrix[-1][-1]

        while left < right:
            mid = (left + right) // 2

            count, smaller, larger = self.count_smaller(matrix, mid, left, right)

            if count == k:
                return smaller
            elif count > k:
                right = smaller
            else:
                left = larger

        return left
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))

# Do binary search in the number range (smallest to largest of the matrix)
# Every time we find a point, find the number of elements smaller than it in the matrix.
# Start from bottom left. If the element is smaller than the middle point then by default, every element before that row
# is smaller, so increment the count by the number of rows up to it. Then move to the right.
# If the element is larger then move up. Each time, keep track of the first elements larger/smaller than the middle.
# Once we have a count, compare it to k. If it's k then return the element smaller than the middle.
# If it's less than k then eliminate the left portion by setting left = larger, otherwise right = smaller (eliminating the right)
# Return left at the end