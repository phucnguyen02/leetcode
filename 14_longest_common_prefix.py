class Solution:
    def longestCommonPrefix(self, strs) -> str:
        shortest = min(strs)
        res = ""
        for i in range(len(shortest)):
            prefix = shortest[:i+1]

            for word in strs:
                if word[:i+1] != prefix:
                    return res
            
            res = prefix
        
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonPrefix(["flower","flow","flight"]))
    print(sol.longestCommonPrefix(["dog","racecar","car"]))


# Use the shortest string as a baseline because any result longer than it will no longer count as a prefix for all strings
# Iterate through each character of the shortest string and use it as a prefix to compare with every other string
# If a prefix doesn't exist in every string then return the previous result
# Otherwise, keep updating the final result corresponding to the longest prefix