import heapq

class Solution:
    def mincostToHireWorkers(self, quality, wage, k: int) -> float:
        wage_to_quality = [(w / q, q) for (w, q) in zip(wage, quality)]
        workers = []
        wage_to_quality.sort()
        total_quality = 0
        res = 1e9
        for wtq, worker_quality in wage_to_quality:
            heapq.heappush(workers, -worker_quality)
            total_quality += worker_quality
            if len(workers) > k:
                qual_pop = heapq.heappop(workers)
                total_quality += qual_pop
            
            if len(workers) == k: res = min(res, wtq * total_quality)
        
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.mincostToHireWorkers([10,20,5], [70, 50, 30], 2))
    print(sol.mincostToHireWorkers([3,1,10,10,1], [4,8,2,2,7], 3))

# For each worker, consider their wage to quality ratio. More specifically, how much is 1 point of quality of theirs worth?
# When comparing 2 workers, we have to consider these ratios. We have to be paying based on the higher ratio because then it'd guarantee we'd be able to pay both of them.
# We first keep track of these ratios by an array, and sort it in ascending order because the lower the ratio, the more cost-effective that worker is
# We also want to minimize the difference between the qualities of the workers/the qualities themselves since they influence the cost so we'll use a max heap.
# The cost would be the product of the total quality and the highest wage to quality ratio within the heap of length k