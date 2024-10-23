class Solution:
    def restoreIpAddresses(self, s: str):
        if len(s) > 12: return []
        res = []
        def backtracking(first, dots, curIP):
            if dots == 3:
                remaining = s[first:]
                if 1 <= len(remaining) <= 3 and remaining:
                    if int(remaining) <= 255 and (first == len(s) - 1 or remaining[0] != "0"):
                        res.append(curIP + s[first:])
                return
            for i in range(first, min(first + 3, len(s))):
                if int(s[first:i+1]) <= 255 and (i == first or s[first] != "0"):
                    backtracking(i + 1, dots + 1, curIP + s[first:i+1] + ".")

        backtracking(0, 0, "")
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.restoreIpAddresses("25525511135"))
    print(sol.restoreIpAddresses("101023"))

# For any index, attempt to put a dot in its position and the 2 positions after. The reason is that the max length of a number is 3 in an IP address.
# That number also has to be less than 255. If the length of the number is not 1 then it can't start with a 0 either. Then backtrack based on that number
# After we've placed 3 dots, we see if the rest of the string is a valid IP number. The length has to be between 1 and 3. If it's 0 then we placed a dot after the string, which is wrong.
# The number has to be less than 255 still and if the length is 1 then it can't start with a 0 either.
# If these are true, add the number along with the current IP to the result array