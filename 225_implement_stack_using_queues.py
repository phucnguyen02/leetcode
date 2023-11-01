class MyStack:

    def __init__(self):
        self.q1 = []
        self.top_elem = -1

    def push(self, x: int) -> None:
        self.q1.append(x)
        self.top_elem = x

    def pop(self) -> int:
        q2 = []
        if len(self.q1) == 1:
            self.top_elem = -1
        while len(self.q1) > 1:
            self.top_elem = self.q1.pop(0)
            q2.append(self.top_elem)
        result = self.q1.pop(0)
        while q2:
            self.q1.append(q2.pop(0))
        return result

    def top(self) -> int:
        return self.top_elem
        

    def empty(self) -> bool:
        return not self.q1
        


# Your MyStack object will be instantiated and called as such:
if __name__ == "__main__":
    obj = MyStack()
    obj.push(3)
    param_2 = obj.pop()
    param_3 = obj.top()
    param_4 = obj.empty()
    print(param_2, param_3, param_4)

#Intuition: Use 1 queue, and another for popping, maintain the top element in a variable
#On push, update the top element and push the element into the first queue
#On pop, pop every element except the last one in the queue and append each to another queue.
#Update top to be the last element popped.
#Pop the remaining item and return it later. Put every element from the second queue back into the first queue. O(n) time
#On top, return top element
#On erase, return if the first queue is empty
#O(1) on everything besides pop, which is O(n)

#Push:
#Append x, top = x

#Pop:
#While length of q1 > 1:
#Top = pop q1, append it into q2
#result = pop q1
#While q2:
#Pop q2, append into q1
#Return result

#Top:
#Return top

#Empty:
#Return length of q1 > 0

#Edge case:
#If queue is empty, set top = -1