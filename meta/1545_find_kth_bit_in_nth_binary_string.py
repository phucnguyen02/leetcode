reverse = {"0": "1", "1": "0"}

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"

        length = 2 ** n
        if k == length // 2:
            return "1"
        
        if k < length // 2:
            return self.findKthBit(n - 1, k)
        
        mirrored_k = length - k
        rev = reverse[self.findKthBit(n - 1, mirrored_k)]
        return rev
        

# For every bit, its mirror through the center point of the string would be its inverse
# We can utilize this to account for previous results
# If a bit is on the left half of the string, find its position in the n - 1 string.
# If a bit is on the right half, return the inverse of its mirror position in the n - 1 string.
# If a bit is in the middle, return "1".
# If n == 1, return "0"