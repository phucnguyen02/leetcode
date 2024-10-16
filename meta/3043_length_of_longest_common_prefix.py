class TrieNode:
    def __init__(self):
        self.children = [None] * 10

class Solution:
    def insert(self, root, num):
        digits = [int(dig) for dig in str(num)]
        curr = root
        for digit in digits:
            if not curr.children[digit]:
                new_node = TrieNode()
                curr.children[digit] = new_node
            curr = curr.children[digit]

    def search(self, root, num):
        digits = [int(dig) for dig in str(num)]
        curr = root
        length = 0
        for digit in digits:
            if not curr.children[digit]:
                return length
            curr = curr.children[digit]
            length += 1
        return length
        
    def longestCommonPrefix(self, arr1, arr2) -> int:
        res = 0
        root = TrieNode()
        for num in arr1:
            self.insert(root, num)

        for num in arr2:
            res = max(self.search(root, num), res)

        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonPrefix([1,10,100], [1000]))
    print(sol.longestCommonPrefix([1,2,3], [4, 4, 4]))

# Use a trie to store all of the prefixes in the first array.
# Go through every number in the second array and traverse the trie for each number. We increase the prefix length every
# time the digit exists in a node's children and keep traversing down. If a child for arr2's number doesn't exist, that's the common prefix
# for that number, so we return the length we got so far. We maximize this length