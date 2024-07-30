from collections import defaultdict
from math import sqrt

class Solution:
    def sieve_of_eratosthenes(self, n):
        prime = [True for i in range(n+1)]
        p = 2
        while p * p <= n:
            if prime[p]:
                for i in range(p * p, n+1, p):
                    prime[i] = False
            p += 1
    
        for p in range(2, n+1):
            if prime[p]:
                self.primes[p] = True

    def nonSpecialCount(self, l: int, r: int) -> int:
        self.primes = defaultdict(bool)
        self.sieve_of_eratosthenes(int(sqrt(r)))
        
        res = r - l + 1
        for prime in self.primes:
            if prime*prime > r:
                break
            
            if l <= prime*prime <= r:
                res -= 1
        
        return res
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.nonSpecialCount(4, 16))
    print(sol.nonSpecialCount(10086764, 96508040))

# Numbers that only have 2 unique positive divisors aside themselves would be squares of primes.
# Use Sieve of Eratosthenes to find all of the primes before square root of r, since that's the maximum possible number within the range.
# For every single of those primes, mark those whose squares are between l and r