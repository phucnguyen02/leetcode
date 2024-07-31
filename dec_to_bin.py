 
class Solution:
    def dec_to_bin(self, x):
        res = ""
        while x:
            res += str(x % 2)
            x //= 2

        return int(res[::-1])
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.dec_to_bin(15))
    print(sol.dec_to_bin(13))