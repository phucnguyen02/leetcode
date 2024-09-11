import math

class Solution:
    def __init__(self):
        self.arr = [9, 4, 13, 2, 1]
    def dumb_sort(self, l, r):
        n = r - l + 1
        print(self.arr[l:r+1])
        if n == 2 and self.arr[l] > self.arr[r]:
            self.arr[l], self.arr[r] = self.arr[r], self.arr[l]

        elif n > 2:
            m = math.ceil(2 * n / 3)
            print(l, r, m, self.arr[l:r+1])
            self.dumb_sort(l, l + m - 1)
            self.dumb_sort(r - m + 1, r)
            self.dumb_sort(l, l + m - 1)
        
        return self.arr

if __name__ == "__main__":
    sol = Solution()
    print(sol.dumb_sort(0, 4))