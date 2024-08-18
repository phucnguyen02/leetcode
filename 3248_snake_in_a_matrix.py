class Solution:
    def finalPositionOfSnake(self, n, commands) -> int:
        res = 0
        for command in commands:
            if command == "UP":
                res -= n
            elif command == "DOWN":
                res += n
            elif command == "RIGHT":
                res += 1
            else:
                res -= 1

        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.finalPositionOfSnake(2, ["RIGHT","DOWN"]))
    print(sol.finalPositionOfSnake(3, ["DOWN","RIGHT","UP"]))