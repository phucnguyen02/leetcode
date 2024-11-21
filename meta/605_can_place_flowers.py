class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        ptr1 = -1
        for ptr2 in range(len(flowerbed)):
            if flowerbed[ptr2] == 1:
                gap = ptr2 - ptr1 - 1
                if ptr1 == -1:
                    gap += 1
                
                n -= ((gap - 1) // 2)

                ptr1 = ptr2
        
        gap = len(flowerbed) - ptr1 - 1
        if ptr1 == -1: gap += 1
        
        n -= (gap // 2)
        return n <= 0

# Find the gaps between every pair of 1s, including the first and last where we account for 1s outside of the array
# If ptr1 == -1 then add 1 to the gap since we have more gap when element 0 can have a flower pot
# Same goes for the last element
