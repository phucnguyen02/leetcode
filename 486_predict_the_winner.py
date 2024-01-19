from collections import defaultdict

class Solution:
    def dp(self, left, right, arr):
        if left == right: return arr[left]

        if (left, right) in self.results: return self.results[(left, right)]

        self.results[(left, right)] = max(arr[left] + sum(arr[left + 1:right + 1]) - self.dp(left + 1, right, arr), arr[right] + sum(arr[left:right]) - self.dp(left, right - 1, arr))
        return self.results[(left, right)]
    
    def predictTheWinner(self, nums) -> bool:
        self.results = defaultdict(int)
        n = len(nums)
        if n <= 2: return True
        optimal_1 = sum(nums[1:n]) - self.dp(1, n - 1, nums)
        optimal_2 = sum(nums[:-1]) - self.dp(0, n - 2, nums)
        max_score = max(nums[0] + optimal_1, nums[-1] + optimal_2)

        print(self.results, max_score)
        return max_score >= sum(nums) - max_score


if __name__ == "__main__":
    sol = Solution()
    print(sol.predictTheWinner([1, 5, 2]))
    print(sol.predictTheWinner([1, 5, 233, 7]))
    print(sol.predictTheWinner([1,2,99]))


# dp -> optimal score of player x, given a subarray.
# dp(1,5,2) -> optimal score of player x, given [1,5,2] -> solves the question
# dp(5,2) -> optimal score of player x, given [5,2] -> the score the player 2 will optimally get, if player 1 picked 1

# what is the score of player 1, if player 2 plays optimally on 5,2 and player 2 starts first. It's actually sum([5,2]) - dp(5,2)



# player 1 starts first, picked 1: total score = 1 + sum(5,2) - dp(5,2)
# player 1 starts first, picked 2: total score = 2 + sum(1,5) - dp(1,5)

# max(1 + sum(5,2) - dp(5,2), 2 + sum(1,5) - dp(1,5)) -> recurrence relation

# given array i->j, calculate recurrence relation

# max(nums[i] + sum(nums[i+1...j]) - dp(i+1,j, nums), nums[j] + sum(nums[i...j-1]) - dp(i,j-1)) -> maximum score
# maximum score > remainder

# key: think about the game state, think of the win condition, and model the DP to the win condition. when it's game state question, prefer recursion.
# also try the other question in EPI and look at answers. 