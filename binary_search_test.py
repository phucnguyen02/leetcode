from time import *

class BinarySearch:
    def __init__(self, k):
        self.k = k

    def valid(self, x):
        return x >= self.k

    def method1(self, arr):
        l = 0
        r = len(arr) - 1
        while l < r:
            m = (l + r) // 2
            if self.valid(arr[m]):
                r = m
            else:
                l = m + 1
        return l

    def method2(self, arr):
        x = -1
        b = len(arr) // 2
        while b >= 1:
            while x + b < len(arr) and not self.valid(arr[x + b]):
                x += b
            b //= 2

        return x + 1

if __name__ == "__main__":
    arr = [0,1,2,3,4,5,6,7,8,9]
    k = 5
    bin_search = BinarySearch(5)
    print(bin_search.method1(arr))
    print(bin_search.method2(arr))