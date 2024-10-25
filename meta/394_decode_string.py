class Solution:
    def __init__(self):
        self.index = 0

    def decodeString(self, s: str) -> str:
        res = ""
        while self.index < len(s) and s[self.index] != "]":
            if not s[self.index].isdigit():
                res += s[self.index]
                self.index += 1
            else:
                count = 0
                while self.index < len(s) and s[self.index].isdigit():
                    count = count * 10 + int(s[self.index])
                    self.index += 1
                
                self.index += 1
                decode = self.decodeString(s)

                self.index += 1
                
                res += decode * count
        return res

# Keep a global index indicating how far along we've traversed in s. If we encounter a character then append it to the result string
# Otherwise, check what the count is, then skip over the opening bracket and call recursion on the string within.
# We process that smaller string until we reach ], then we return. The string outside would get the inner string * count, and we skip over the ] bracket
# so that we can continue processing
