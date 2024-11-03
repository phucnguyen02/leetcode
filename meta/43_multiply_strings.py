class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = 0
        power_out = 1
        for i in range(len(num2) - 1, -1, -1):
            power_in = 1
            inner_sum = 0
            for j in range(len(num1) - 1, -1, -1):
                prod = int(num1[j]) * int(num2[i]) * power_in
                inner_sum += prod
                power_in *= 10

            res += inner_sum * power_out
            power_out *= 10

        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.multiply("123", "456"))

# Multiply a multiplier by 10 every time we move to the left