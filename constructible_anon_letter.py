from collections import *

class Solution:
    def construct_anon_letter(self, letter, magazine):
        magazine_count = Counter(magazine)
        letter_count = Counter(letter)
        for char in magazine_count:
            if char in letter_count and magazine_count[char] < letter_count[char]:
                return False
        for char in letter_count:
            if char not in magazine_count: return False
        return True



if __name__ == "__main__":
    sol = Solution()
    print(sol.construct_anon_letter("isfghisufhiusf", "if"))
    print(sol.construct_anon_letter("iiiddddfff", "iiiiiiidddddddssssssfff"))


#Letter can only be constructed from magazine if every character in letter exists in magazine
#and if the character exists in magazine, magazine must have a high enough frequency of said character


#Pseudocode:
#Get counts of every character in both magazine and letter
#Check if every character in letter exists in magazine
#Check if the character exists in magazine, its count is larger than or equal to the count of the same character in letter
#Return true if the above 2 are satisfied, false otherwise