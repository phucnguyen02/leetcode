class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) > len(num2):
            num1, num2 = num2, num1

        ptr1 = len(num1) - 1
        ptr2 = len(num2) - 1
        res = ""
        carry = 0
        sum = 0
        while ptr1 >= 0:
            sum = int(num1[ptr1]) + int(num2[ptr2]) + carry
            carry, digit = divmod(sum, 10)
            res = str(digit) + res
            ptr1 -= 1
            ptr2 -= 1
        
        while ptr2 >= 0:
            sum = int(num2[ptr2]) + carry
            carry, digit = divmod(sum, 10)
            res = str(digit) + res
            ptr2 -= 1

        return res if carry == 0 else "1" + res
    
# Do 2 pointers iterating backwards from each num. Take note of the carry when the sum > 10.
# Swap num2 with num1 if len(num1) is larger so num2 is always larger. It's easier to iterate when 1 pointer runs out that way
