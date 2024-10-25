import heapq

class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
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
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))
        