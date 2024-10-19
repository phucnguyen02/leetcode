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


# Iterate through the abbreviation because it might be longer than the word. Have 2 pointers for the word and the abbreviation.
# If ptr2 is a digit then keep track of the number formed by the digits. If the number starts at 0 then it's invalid.
# Add that number to ptr1
# If ptr1 exceeds the word length before ptr2 finishes or the letters at the indices don't match then return false. Otherwise increment both.
# We return whether we've reached the end of the word exactly
