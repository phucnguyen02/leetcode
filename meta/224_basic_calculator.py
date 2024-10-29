class Solution:
    def __init__(self):
        self.index = 0

    def calc(self, s):
        res = 0
        num = 0
        last_result = 0
        op = "+"
        while self.index < len(s):
            if s[self.index] == ")":
                res += last_result
                last_result = num if op == "+" else -num
                break

            if s[self.index] == " ":
                self.index += 1
                continue

            if s[self.index].isdigit():
                num = num * 10 + int(s[self.index])
            elif s[self.index] in "+-":
                res += last_result
                last_result = num if op == "+" else -num
                num = 0
                op = s[self.index]
            else:
                self.index += 1
                num = self.calc(s)

            self.index += 1
        return res + last_result 

    def calculate(self, s: str) -> int:
        return self.calc(s + "+")
        

# Use a variable to store the previous operation. By default it should be +. Each time we come across a new operation,
# we finish the previous operation and storing the result. Every time we come across + or -, we update the final result with
# it since it has to be sequential. We add a + onto the string to make sure it finished the previous operation, before adding the last result to the final result.
# Every time we reach an open bracket, do a recursion call to get the inner result, and set the num to be that result. If we see a closing bracket, treat
# it similarly to the + we add onto the end of the string