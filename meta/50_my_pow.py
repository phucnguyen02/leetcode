class Solution:
    def calc_power(self, x, n):
        if n == 0: return 1.0
        if n == 1: return x
        div = self.calc_power(x, n // 2)
        if n % 2 == 0:
            return div * div
        return div * div * x
    
    def myPow(self, x: float, n: int) -> float:
        return self.calc_power(x, n) if n >= 0 else self.calc_power(1/x, -n)

if __name__ == "__main__":
    sol = Solution()
    print(sol.myPow(2.0000, 10))
    print(sol.myPow(2.0000, -2))

# The recurrence relation is x^n = x^(n/2) * x^(n/2), multiplied by x if n is odd. We use recursion in order to simulate this
# and solve the problem in O(logn)