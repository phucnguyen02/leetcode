from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end = False

class Solution:
    def removeSubfolders(self, folder):
        root = TrieNode()
        res = set()
        for subfolder in folder:
            cur = root
            directories = subfolder.split("/")
            for ch in directories:
                if ch not in cur.children:
                    cur.children[ch] = TrieNode()
                
                cur = cur.children[ch]

            cur.is_end = True
        
        for subfolder in folder:
            cur = root
            directories = subfolder.split("/")
            path = []
            for ch in directories:
                cur = cur.children[ch]
                path.append(ch)
                if cur.is_end:
                    res.add("/".join(path))
                    break
        return list(res)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"]))