class Solution:
    def stringHash(self, s: str, k: int) -> str:
        n = len(s)
        res = ""
        letters = {chr(i + 97): i for i in range(26)}
        numbers = {i: chr(i + 97) for i in range(26)}
        for i in range(n // k):
            sum = 0
            for j in range(i * k, i * k + k):
                sum += letters[s[j]]

            sum %= 26
            res += numbers[sum]
        
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.stringHash("abcd", 2))
    print(sol.stringHash("mxz", 3))