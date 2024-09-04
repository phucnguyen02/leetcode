class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        num1, num2, num3 = str(num1), str(num2), str(num3)
        num1 = "0" * (4 - len(num1)) + num1
        num2 = "0" * (4 - len(num2)) + num2
        num3 = "0" * (4 - len(num3)) + num3
        res = ""
        for i in range(4):
            res += str(min(int(num1[i]), int(num2[i]), int(num3[i])))
        
        return int(res)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.generateKey(1, 10, 1000))
    print(sol.generateKey(987, 879, 798))
    print(sol.generateKey(1, 2, 3))