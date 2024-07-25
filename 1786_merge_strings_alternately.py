class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        turn = 1
        ptr1 = ptr2 = 0
        res = ""
        while ptr1 < len(word1) and ptr2 < len(word2):
            if turn == 1:
                res += word1[ptr1]
                ptr1 += 1
            else:
                res += word2[ptr2]
                ptr2 += 1
            turn *= -1

        while ptr1 < len(word1):
            res += word1[ptr1]
            ptr1 += 1

        while ptr2 < len(word2):
            res += word2[ptr2]
            ptr2 += 1
        
        return res


# Use 2 pointers to keep track of where we are in the words, use a turn counter that alternates between 1 and -1 to know which word comes next