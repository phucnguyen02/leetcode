import heapq

class Solution:
    def resultsArray(self, queries, k: int):
        n = len(queries)
        res = [-1]*n
        heap = []
        
        for i in range(len(queries)):
            query = queries[i]
            dist = abs(query[0]) + abs(query[1])
            heapq.heappush(heap, -dist)
            if len(heap) > k:
                heapq.heappop(heap)

            if len(heap) == k:
                elem = -heapq.heappop(heap)
                res[i] = elem
                heapq.heappush(heap, -elem)
        
        return res
if __name__ == "__main__":
    sol = Solution()
    print(sol.resultsArray([[1,2],[3,4],[2,3],[-3,0]], 2))
    print(sol.resultsArray([[5,5],[4,4],[3,3]], 1))

# Use a max heap with size k to keep track of the k-th smallest distance. When the size of the heap exceeds k then
# we pop the head because it's no longer among the smallest distances 