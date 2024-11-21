class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        
        L = len(beginWord)
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)
        seen = set()
        dq = deque([(beginWord, 1)])
        
        while dq:
            word, distance = dq.popleft()
            if word == endWord: return distance
            for i in range(L):
                inter = word[:i] + "*" + word[i+1:]
                
                for neighbor in all_combo_dict[inter]:
                    if neighbor in seen:
                        continue

                    seen.add(neighbor)
                    dq.append((neighbor, distance + 1))
        return 0
            
# For each word, store words it can transform to in a hash table, like a template. For example, abc, abd are stored in ab* together, but not a*c
# Use BFS with the word as the starting node, add all words it can transform into in a queue, end when we find the endWord