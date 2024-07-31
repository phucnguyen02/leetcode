 
class Solution:
    def bin_to_dec(self, x):
        x = str(x)
        res = 0
        for (i, num) in enumerate(x):
            res += int(num) * (2 ** (len(x) - i - 1))
        
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.bin_to_dec(1110))