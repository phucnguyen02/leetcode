class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr1 = ptr2 = 0
        while ptr1 < len(s) and ptr2 < len(t):
            if t[ptr2] == s[ptr1]:
                ptr1 += 1
            
            ptr2 += 1
        return ptr1 == len(s)
    
# Just use 2 pointers. Increment the s pointer everytime there's a match in t. If the s pointer makes it all the way to the end, it is a subsequence