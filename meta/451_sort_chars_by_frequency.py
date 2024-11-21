class Solution:
    def frequencySort(self, s: str) -> str:
        sort_count = sorted([(val, ch) for (ch, val) in Counter(s).items()], reverse=True)
        res = ""
        for (val, ch) in sort_count:
            res += val * ch
        return res
    
# Sort characters by counters in reverse