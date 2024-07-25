from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.arr = deque()
        

    def next(self, val: int) -> float:
        self.arr.append(val)
        if len(self.arr) > self.size:
            self.arr.popleft()
        
        return sum(self.arr) / len(self.arr)
    
# Use deque to pop and insert elements at O(1).
# Use current size of deque to make sure it's within the allotted size
# Calculate the average from there