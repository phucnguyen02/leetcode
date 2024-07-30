class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        turn = 1
        while y > 3 and x > 0:
            turn *= -1
            y -= 4
            x -= 1
        
        return "Alice" if turn == -1 else "Bob"


if __name__ == "__main__":
    sol = Solution()
    print(sol.losingPlayer(2, 7))
    print(sol.losingPlayer(4, 11))

# Each turn, 1 75 coin and 4 10 coins are taken away. Play until you can't take away both at once
