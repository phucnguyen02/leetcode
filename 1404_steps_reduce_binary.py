class Solution:
    def numSteps(self, s: str) -> int:
        carry = 0
        res = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "1":
                if i == 0: break
                if carry == 1:
                    res += 1
                else:
                    res += 2
                carry = 1
            else:
                if carry == 1:
                    res += 2
                else:
                    res += 1
                    carry = 0
        
        return res + carry



if __name__ == "__main__":
    sol = Solution()
    print(sol.numSteps("1101"))
    print(sol.numSteps("1"))
    print(sol.numSteps("10"))

# We move through the string from right to left. If the current bit is 1 then the number is odd, so we need to take 2 steps to remove it. Otherwise we only need 1.
# But it's more complicated than that. We need to worry about bitwise additions. If the current bit is 1 and we add 1 to it, we need to save that carry for a previous
# bit. For example, if we have 01, then the first bit becomes 1 after addition. Because of that, we need 2 steps to remove it.

# If the first bit of the string is 1 then depending on the carry, we get the result. If there is no carry then every operation we did before that has led to the string
# having just the first bit 1, so we are done. Otherwise, we end up with 1 + 1 = 10, so we need an extra operation to remove that 0. Thus, result + carry is our final result.

#   if s[i] == "1" then
#       if carry == 1 then steps += 1 else steps += 2
#       carry = 1

#   else then
#       if carry == 1 then steps += 2, carry = 1 else steps += 1, carry = 0