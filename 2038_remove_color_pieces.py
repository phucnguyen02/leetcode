class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        legal_A = 0
        legal_B = 0

        consecutive_A = 0
        consecutive_B = 0
        for letter in colors:
            if letter == "A":
                legal_B += max(0, consecutive_B - 2)
                consecutive_B = 0
                consecutive_A += 1

            else:
                legal_A += max(0, consecutive_A - 2)
                consecutive_A = 0
                consecutive_B += 1

        legal_A += max(0, consecutive_A - 2)
        legal_B += max(0, consecutive_B - 2)

        return legal_A > legal_B

if __name__ == "__main__":
    sol = Solution()
    print(sol.winnerOfGame("AAABABB"))
    print(sol.winnerOfGame("AA"))
    print(sol.winnerOfGame("ABBBBBBBAAA"))


# One player's move does not dictate the other's, since a player is only allowed to move a character that's between the same 2 characters,
# so only that area would be affected.
    
# The total number of legal moves is the total number of consecutive characters that's longer than 3, and minus 2 for each.
# Return whether the total number of legal moves of Alice is strictly larger than Bob, because if they're equal then Bob
# can still pass back after his last legal move and Alice would lose.
    
# legal_A = consecutive_A that's more than 2 - total number of legal sequences of A
# legal_B = consecutive_B that's more than 2 - total number of legal sequences of B
# return legal_A > legal_B