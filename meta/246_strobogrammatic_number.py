class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        reverse = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        new_num = ""
        for ch in num:
            if ch not in reverse: return False
            new_num += reverse[ch]
        return new_num[::-1] == num
    
# Store a dict for corresponding upside down values. Iterate through string, append the upside down values.
# If a number is not in the upside down list, return false. 
# Return whether the reversed new num is equal to the num at the end.