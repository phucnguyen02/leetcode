class Solution:
    def sortedSquares(self, nums):
        negatives = []
        positives = []
        for num in nums:
            if num < 0: negatives.append(num)
            else: positives.append(num)

        res = []

        negatives.reverse()
        
        ptr1 = ptr2 = 0
        while ptr1 < len(negatives) and ptr2 < len(positives):
            if negatives[ptr1] ** 2 < positives[ptr2] ** 2:
                res.append(negatives[ptr1] ** 2)
                ptr1 += 1
            else:
                res.append(positives[ptr2] ** 2)
                ptr2 += 1

        while ptr1 < len(negatives):
            res.append(negatives[ptr1] ** 2)
            ptr1 += 1
        
        while ptr2 < len(positives):
            res.append(positives[ptr2] ** 2)
            ptr2 += 1

        return res