from collections import defaultdict
from random import randrange

class Solution:

    def __init__(self, nums):
        self.indices = defaultdict(list)
        for (i, num) in enumerate(nums):
            self.indices[num].append(i)


    def pick(self, target: int) -> int:
        if len(self.indices[target]) == 1:
            return self.indices[target][0]
        
        rand_index = randrange(0, len(self.indices[target]))
        return self.indices[target][rand_index]
        

# Store all the indices within a hash table list corresponding to a number.
# If there's multiple, do randrange to pick a random index from 0 to that number's indices length
