class Backtracking:
    def __init__(self, arr):
        self.arr = arr
        self.result = []

    def backtracking(self, first, curr, max_size):
        if len(curr) == max_size:
            self.result.append(curr[:])
        
        for i in range(first, len(self.arr)):
            curr.append(self.arr[i])
            self.backtracking(i + 1, curr, max_size)
            curr.pop()
        
if __name__ == "__main__":
    arr = [1, 3, 4]
    backtrack = Backtracking(arr)
    backtrack.backtracking(0, [], 2)
    print(backtrack.result)