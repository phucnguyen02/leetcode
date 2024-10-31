class Solution:
    def isAlienSorted(self, words, order: str) -> bool:
        letters = {letter: i for (i, letter) in enumerate(order)}
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    if letters[d] < letters[c]:
                        return False
                    else:
                        break
            else:
                if len(second_word) < len(first_word): return False

        return True
        
        
# Hash table to store the indices of every letter in the order
# Compare every consecutive pair in the words, and the letters at each index. If the second letter is before the first letter in the order, return false
# Otherwise, break the for loop
# If we make it through the for loop, verify that the first word is shorter than the second since the second could be a prefix