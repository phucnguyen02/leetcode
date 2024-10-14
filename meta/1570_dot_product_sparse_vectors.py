class SparseVector:
    def __init__(self, nums):
        self.nonzeros = []
        for (i, num) in enumerate(nums):
            if num:
                self.nonzeros.append((i, num))
        
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ptr1 = ptr2 = 0
        res = 0
        while ptr1 < len(self.nonzeros) and ptr2 < len(vec.nonzeros):
            if self.nonzeros[ptr1][0] == vec.nonzeros[ptr2][0]:
                res += self.nonzeros[ptr1][1] * vec.nonzeros[ptr2][1]
                ptr1 += 1
                ptr2 += 1
            
            elif self.nonzeros[ptr1][0] < vec.nonzeros[ptr2][0]:
                ptr1 += 1

            elif self.nonzeros[ptr1][0] > vec.nonzeros[ptr2][0]:
                ptr2 += 1

        return res

# Store the nonzeros of a sparse vector in a hash map because it's the most efficient.
# When calculating the dot product, take the current hash map and see if any of the indices exist in the other vector's nonzeros hash map,
# then multiply accordingly.

# Alternatively, store (index, value) tuples in a list for nonzero values and use 2 pointers to traverse both vectors. Make sure the indices are equal at all times

