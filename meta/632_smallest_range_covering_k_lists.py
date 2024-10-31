class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = [(lst[0], i, 0) for (i, lst) in enumerate(nums)]
        k = len(nums)
        max_val = max([nums[i][0] for i in range(k)])
        heapq.heapify(heap)
        left_res = -1e9
        right_res = 1e9
        
        while len(heap) == k:
            min_val, lst_idx, idx = heapq.heappop(heap)

            if max_val - min_val < right_res - left_res:
                left_res = min_val
                right_res = max_val

            if idx + 1 < len(nums[lst_idx]):
                heapq.heappush(heap, (nums[lst_idx][idx + 1], lst_idx, idx + 1))
                max_val = max(max_val, nums[lst_idx][idx + 1])

        return [left_res, right_res]
    
# It's merge K sorted lists. The heap always contains k elements so we find the min and max within the heap. The min is always the top,
# and the max is always the max of the current max and any element we push into the heap