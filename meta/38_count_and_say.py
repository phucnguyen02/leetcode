class Solution:
    def RLE(self, s):
        res = ""
        count = 1
        cur_ch = None
        for (i, ch) in enumerate(s):
            if ch != cur_ch:
                if cur_ch: res += str(count) + cur_ch
                count = 1
                cur_ch = ch
            else:
                count += 1

        return res + str(count) + cur_ch
    def countAndSay(self, n: int) -> str:
        if n == 1: return "1"
        cur = "1"
        for i in range(2, n + 1):
            next = self.RLE(cur)
            cur = next

        return cur
if __name__ == "__main__":
    sol = Solution()
    print(sol.countAndSay(1))
    print(sol.countAndSay(3))

# Have a function that converts a string into its RLE encoding. Iterate through it and keep track of the count of the current character.
# If we move to a new character, append the count + the character into the encoding.