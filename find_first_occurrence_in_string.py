class Solution:
    def calculate_hash(self, string):
        res = 0
        prime = 29
        modulo = 10 ** 9 + 7
        for i in range(len(string)):
            res += ord(string[i]) * ((prime ** i) % modulo)
            res %= modulo
        
        return res

    def find_first_occurrence(self, text, pattern) -> int:
        prime = 29
        modulo = 10 ** 9 + 7
        pattern_length = len(pattern)
        text_length = len(text)
        pattern_hash = self.calculate_hash(pattern)
        text_hash = self.calculate_hash(text[:pattern_length])

        # Base case at index 0
        if text_hash == pattern_hash and text[:pattern_length] == pattern: return 0

        for i in range(1, text_length - pattern_length + 1):
            text_hash -= ord(text[i - 1])
            text_hash //= prime
            text_hash += ord(text[i + pattern_length - 1]) * ((prime ** (pattern_length - 1)) % modulo)
            text_hash %= modulo
            
            if text_hash == pattern_hash and text[i:i + pattern_length] == pattern: return i

        return -1
        


if __name__ == "__main__":
    sol = Solution()
    print(sol.find_first_occurrence("haahahsdasdasdiuhaiushdaisdh", "iuhai"))
    

# Use Rabin-Karp/Rolling Hash for this

# Formula:
# char: a = 1, b = 2, ..., z = 26

# x = old_hash - val(old_char)
# x /= prime
# x += prime^(m - 1) * val(new_char) with m being the length of the pattern

# Compare newly calculated hash with the hash of the pattern. If there's a match, compare the substring and the pattern. Return the index if they match.
