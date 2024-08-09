class Solution:
    def sortEvenOdd(self, nums):
        odds = []
        evens = []
        for (i, num) in enumerate(nums):
            if i % 2 == 0:
                evens.append(num)
            else:
                odds.append(num)

        turn = 1
        evens.sort()
        odds.sort(reverse=True)
        ptr1 = ptr2 = 0

        res = []
        while ptr1 < len(evens) and ptr2 < len(odds):
            if turn == 1:
                res.append(evens[ptr1])
                ptr1 += 1
            else:
                res.append(odds[ptr2])
                ptr2 += 1
            
            turn *= -1
        
        if ptr1 < len(evens): res.append(evens[ptr1])
        if ptr2 < len(odds): res.append(odds[ptr2])

        return res
    
# Merge sorted arrays but with evens and odd indices instead