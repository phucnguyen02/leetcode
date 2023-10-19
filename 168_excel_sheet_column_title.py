import string
import sys 

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber > 0:
            columnNumber -= 1
            res += chr(columnNumber % 26 + 65)
            columnNumber //= 26
        return res[::-1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.convertToTitle(704))


#Intuition:
#Find the number's modulo with 26, which will return the last letter
#Divide the number by 26 in order to remove the last letter
