from functools import cmp_to_key

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class AutocompleteSystem:
    def insert(self, sentence):
        cur = self.root
        for ch in sentence:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            
            cur = cur.children[ch]

        cur.is_end = True

    def update_input(self, ch):
        if self.invalid: return

        if ch not in self.input_node.children:
            self.invalid = True
        else:
            self.input_node = self.input_node.children[ch]
        
    def get_all_children(self, node, word):
        if node.is_end:
            self.word_list.append(word)
        
        if not node.children:
            return

        for children in node.children:
            self.get_all_children(node.children[children], word + children)

    def compare(self, sentence1, sentence2):
        if sentence1[0] < sentence2[0]:
            return 1
        elif sentence1[0] > sentence2[0]:
            return -1
        
        if sentence1[1] < sentence2[1]:
            return -1
        elif sentence1[1] > sentence2[1]:
            return 1
        
        return 0
        
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.frequencies = {sentence: time for (sentence, time) in zip(sentences, times)}
        for sentence in sentences:
            self.insert(sentence)

        self.input_so_far = ""
        self.input_node = self.root
        self.invalid = False
        self.word_list = []

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.insert(self.input_so_far)
            if self.input_so_far not in self.frequencies:
                self.frequencies[self.input_so_far] = 0
            self.frequencies[self.input_so_far] += 1
            
            self.input_so_far = ""
            self.input_node = self.root
            self.invalid = False

            return []
        
        self.input_so_far += c
        self.update_input(c)

        if self.invalid: return []
        self.get_all_children(self.input_node, self.input_so_far)
        
        child_sentences = []
        for word in self.word_list:
            child_sentences.append((self.frequencies[word], word))

        child_sentences = sorted(child_sentences, key=cmp_to_key(self.compare))
        res = []
        for i in range(min(3, len(child_sentences))):
            res.append(child_sentences[i][1])
        self.word_list = []
        return res


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)

# Put all the sentences into a trie
# Store sentence frequencies in a hash table
# We have a node corresponding to the user input sentence.
# Each time a character c is taken in, we add it to a string called input_so_far. We'd also attempt to move the input node.
# If the character we added makes the input not a prefix of any of the sentences, then we no longer want to traverse the trie based on that sentence.
# We set a flag to see if this is true or not. If it's true then return [] every time.
# Otherwise, check all strings in the trie that has input_so_far as a prefix, aka do dfs with the latest character as the root.
# Once we have all the children, we sort their frequencies based on the hash table and find the top 3
# If the user inputs "#" then we add input_so_far into the trie and increment its count in the hash_table (0 by default), and reset input_so_far to be empty.

# Potential optimization:
# Instead of doing DFS every time we add a new character, we do DFS on the first character of the input and store all of its children.
# After that, every time we add a new character, we check every children to see if the new character would prevent the input string from being a prefix of any of them.
