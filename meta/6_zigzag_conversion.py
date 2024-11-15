class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        rows = [[] for _ in range(numRows)]
        ptr = 0
        pos = -1
        while ptr < len(s):
            while ptr < len(s) and pos + 1 < numRows:
                pos += 1
                rows[pos].append(s[ptr])
                ptr += 1

            while ptr < len(s) and pos - 1 >= 0:
                pos -= 1
                rows[pos].append(s[ptr])
                ptr += 1

        res = ""
        for row in rows:
            res += "".join(row)
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.convert("PAYPALISHIRING", 3))
    print(sol.convert("PAYPALISHIRING", 4))
    print(sol.convert("A", 1))
            