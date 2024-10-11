class SparseVector:
    def __init__(self, nums):
        self.nonzeros = {}
        for (i, num) in enumerate(nums):
            if num:
                self.nonzeros[i] = num
        
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for index in self.nonzeros:
            if index in vec.nonzeros:
                res += self.nonzeros[index] * vec.nonzeros[index]

        return res
    

# Store the nonzeros of a sparse vector in a hash map because it's the most efficient.
# When calculating the dot product, take the current hash map and see if any of the indices exist in the other vector's nonzeros hash map,
# then multiply accordingly.

