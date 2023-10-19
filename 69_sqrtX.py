class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        r = x
        while l < r:
            m = (l + r) // 2
            if m*m >= x:
                r = m
            else:
                l = m + 1
        return l if l*l == x else l-1


if __name__ == "__main__":
    sol = Solution()
    print(sol.mySqrt(4))
    print(sol.mySqrt(10))


#[1,2,3,4,5,6,7,8,9]
#Find largest x such that x*x < n. Answer should be x+1, but since we're rounding down, it could be x if (x+1)^2 > n