class Solution:
    def convertDateToBinary(self, date: str) -> str:
        dates = date.split("-")
        res = ""
        for day in dates:
            res += str(bin(int(day))[2:])
            res += "-"
        
        return res[:-1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.convertDateToBinary("2080-02-29"))