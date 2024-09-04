class Solution:
    def color(self, coordinate):
        col = coordinate[0]
        row = int(coordinate[1])
        col_to_num = {chr(i + 97): i for i in range(8)}
        if row % 2 == 0:
            return "black" if col_to_num[col] % 2 != 0 else "white"
        
        return "black" if col_to_num[col] % 2 == 0 else "white"

    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        return self.color(coordinate1) == self.color(coordinate2)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.checkTwoChessboards("a1", "c3"))
    print(sol.checkTwoChessboards("a1", "h3"))

# Translate each letter to a number so that we can associate an even row and an odd column with black and even column with white. Same with an odd row.