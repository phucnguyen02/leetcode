class Solution:
    def letterCombinations(self, digits: str):
        if not digits: return []
        digit_letters =  {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                          "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        def backtracking(index = 0, combination = ""):
            if index == len(digits):
                res.append(combination)
                return
            
            for i in range(len(digit_letters[digits[index]])):
                combination += digit_letters[digits[index]][i]
                backtracking(index + 1, combination)
                combination = combination[:-1]

        backtracking()
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.letterCombinations("23"))
    print(sol.letterCombinations(""))
    print(sol.letterCombinations("2"))

# Use the backtracking algorithm
# For each digit, go through every possible letter it can be, and move onto the next index and repeat the process until the end of the array.
# Then we move back and try another combination