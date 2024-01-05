from collections import defaultdict

class Solution:
    def __init__(self):
        self.results = defaultdict(int)
        self.lines = defaultdict(int)

    def recursion_helper(self, words, max_width, line):
        if len(words) == 0: return 0
        if len(words) == 1: return (max_width - len(words[0])) ** 2

        if tuple(words) in self.results: return self.results[tuple(words)]
        res = 1e9

        for i in range(len(words)):
            remaining = max_width
            messiness = 0

            for j in range(len(words) - 1, max(-1, len(words) - i - 2), -1):
                remaining -= len(words[j])
            
            remaining -= i

            if remaining < 0: break
            messiness += remaining ** 2

            min_line = self.recursion_helper(words[:-i-1], max_width, line + 1) + messiness
            if res > min_line:
                self.lines[line] = messiness
            res = min(res, min_line)

        self.results[tuple(words)] = res
        
        return res

    def pretty_printing(self, words, max_width) -> int:
        return self.recursion_helper(words, max_width, 0)


if __name__ == "__main__":
    sol = Solution()
    print(sol.pretty_printing(["I", "have", "inserted", "a", "large", "number", "of", "new", "examples", "from",
    "the", "papers", "for", "the", "Mathematical", "Tripos", "during", "the", "last", "twenty", "years,", "which", "should",
    "be", "useful", "to", "Cambridge", "students"], 36))
    print(sol.pretty_printing(["a", "b", "c", "d"], 5))
