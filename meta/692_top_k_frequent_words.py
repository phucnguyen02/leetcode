import heapq
from collections import Counter

class Pair:
    def __init__(self, word, count):
        self.word = word
        self.count = count

    def __lt__(self, p):
        return self.count < p.count or (self.count == p.count and self.word > p.word)

class Solution:
    def topKFrequent(self, words, k: int):
        count = Counter(words)
        freq = [Pair(word, cnt) for (word, cnt) in count.items()]
        heap = []
        for i in range(len(freq)):
            heapq.heappush(heap, freq[i])
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        while heap:
            res.append(heapq.heappop(heap).word)
        return res[::-1]
    
# Create a custom class with a custom __lt__ comparator so we can compare between 2 pairs of word, cnt. 1 pair is less than the other is its count is smaller, or
# its word is bigger when their counts are equal
# Use a min heap of size k to store the k most frequent strings