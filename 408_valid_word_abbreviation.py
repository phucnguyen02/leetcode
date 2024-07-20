class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if len(abbr) > len(word): return False
        ptr1 = 0
        ptr2 = 0
        while ptr2 < len(abbr):
            if abbr[ptr2].isdigit():
                if abbr[ptr2] == "0": return False
                origin = ptr2
                while ptr2 < len(abbr) and abbr[ptr2].isdigit():
                    ptr2 += 1
                ptr1 += int(abbr[origin:ptr2])
            else:
                if ptr1 >= len(word) or word[ptr1] != abbr[ptr2]: return False
                
                ptr1 += 1
                ptr2 += 1

        return ptr1 == len(word)

        
if __name__ == "__main__":
    sol = Solution()
    # print(sol.validWordAbbreviation("internationalization", "i12iz4n"))
    # print(sol.validWordAbbreviation("apple", "a2e"))
    print(sol.validWordAbbreviation("internationalization", "i5a11o1"))

