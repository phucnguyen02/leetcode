from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums, k: int):
        count = Counter(nums)
        freq = [(cnt, num) for (num, cnt) in count.items()]
        heap = []
        heap = freq[:k]
        heapq.heapify(heap)
        
        for (cnt, num) in freq[k:]:
            if cnt > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (cnt, num))

        return [hp[1] for hp in heap]
if __name__ == "__main__":
    sol = Solution()
    print(sol.topKFrequent([1,1,1,2,2,3], 2))

# Quickselect for O(N)