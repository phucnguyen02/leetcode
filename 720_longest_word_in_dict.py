class Solution:
    def longestWord(self, words) -> str:
        prefixes = set(words)
        res = ""

        for word in words:
            flag = True
            for i in range(len(word)):
                if word[:i + 1] not in prefixes:
                    flag = False
                    break
            
            if flag:
                if len(word) == len(res): res = min(res, word)
                elif len(word) > len(res): res = word
        return res
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestWord(["w","wo","wor","worl","world"]))
    print(sol.longestWord(["a","banana","app","appl","ap","apply","apple"]))
    print(sol.longestWord(["b","br","bre","brea","break","breakf","breakfa","breakfas","breakfast","l","lu","lun","lunc","lunch","d","di","din","dinn","dinne","dinner"]))