class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False
        concat = s + s
        return concat.find(goal) != -1
    
# If the lengths are different then return false
# Concatenate s and s together. If goal isn't a substring in the concatenated string then return false