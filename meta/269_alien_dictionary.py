class Solution:
    def alienOrder(self, words: List[str]) -> str:
        degree = {}
        neighbors = defaultdict(set)
        for word in words:
            for ch in word:
                degree[ch] = 0

        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in neighbors[c]:
                        neighbors[c].add(d)
                        degree[d] += 1
                    break
            else:
                if len(second_word) < len(first_word): return ""

        res = []
        queue = deque([d for d in degree if degree[d] == 0])
        while queue:
            ch = queue.popleft()
            for neighbor in neighbors[ch]:
                degree[neighbor] -= 1
                if degree[neighbor] == 0:
                    queue.append(neighbor)
            res.append(ch)
        
        return "".join(res) if len(res) == len(degree) else ""
    
# For any 2 words, if the 2 letters at the same index of both words are not the same, then the one that goes first has an edge to the other in a graph.
# Otherwise, keep iterating. Add a check to make sure one isn't the prefix of the other 
# Do toposort based on that info

        