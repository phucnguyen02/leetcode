from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        count_letter = Counter(s)
        freq = [(-val, letter) for (letter, val) in count_letter.items()]
        heapq.heapify(freq)

        res = ""
        while len(freq) > 1:
            val_first, first = freq.pop(0)
            val_second, second = freq.pop(0)

            val_first += 1
            val_second += 1
            res += first + second

            if val_first != 0:
                heapq.heappush(freq, (val_first, first))
            
            if val_second != 0:
                heapq.heappush(freq, (val_second, second))

            heapq.heapify(freq)

        if not freq: return res
        if len(freq) == 1 and freq[0][0] == -1: return res + freq[0][1]
        return ""
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.reorganizeString("aab"))
    print(sol.reorganizeString("aaab"))
    print(sol.reorganizeString("vvvlo"))
    print(sol.reorganizeString("zrhmhyevkojpsegvwolkpystdnkyhcjrdvqtyhucxdcwm"))

# Have a heap that stores the counts of all the letters in the original string
# Alternately place the 2 most frequent letters of the string at a time
# If the heap is empty, return the string
# If the heap has 1 element left and that element's frequency is 1, add it to the string and return it
# Return an empty string otherwise