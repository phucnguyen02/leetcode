class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.median = 1e9
    def addNum(self, num: int) -> None:
        if num <= self.median:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        if len(self.max_heap) - len(self.min_heap) == 2:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        elif len(self.min_heap) - len(self.max_heap) == 1:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

        if len(self.max_heap) == len(self.min_heap):
            self.median = (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            self.median = -self.max_heap[0]

    def findMedian(self) -> float:
        return self.median


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# Similar to sliding window median, keep a max and min heap. Ensure that the difference between the lengths of the 2 heaps never exceeds 2,
# with the length of max heap always being no less than the length of the min heap. 