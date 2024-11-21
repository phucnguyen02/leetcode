import heapq

class SeatManager:

    def __init__(self, n: int):
        self.heap = []
        self.ptr = 1

    def reserve(self) -> int:
        if self.heap:
            return heapq.heappop(self.heap)
        
        seat = self.ptr
        self.ptr += 1
        return seat
        

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.heap, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)

# Use a heap to keep track of the smallest unreserved seat
# Use a pointer to move to the next unreserved seat