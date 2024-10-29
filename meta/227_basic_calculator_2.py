class Solution:
    # def calculate(self, s: str) -> int:
    #     stack = []
    #     operation = '+'
    #     cur_num = 0
    #     for ch in s + '+':
    #         if ch == ' ':
    #             continue
    #         if ch.isdigit():
    #             cur_num = cur_num * 10 + int(ch)
    #         if not ch.isdigit():
    #             if operation == '+':
    #                 stack.append(cur_num)
    #             elif operation == '-':
    #                 stack.append(-cur_num)
    #             elif operation == '*':
    #                 stack.append(stack.pop() * cur_num)
    #             elif operation == '/':
    #                 stack.append(int(stack.pop() / cur_num))
    #             cur_num = 0
    #             operation = ch
    #     return sum(stack)

    def calculate(self, s: str) -> int:
        operation = '+'
        cur_num = 0
        res = 0
        last_result = 0
        for (i, ch) in enumerate(s):
            if ch == ' ':
                continue
            if ch.isdigit():
                cur_num = cur_num * 10 + int(ch)
            if not ch.isdigit() or i == len(s) - 1:
                print(ch, operation, res, last_result)
                if operation == '+' or operation == '-':
                    res += last_result
                    last_result = cur_num if operation == '+' else -cur_num
                elif operation == '*':
                    last_result *= cur_num
                elif operation == '/':
                    last_result = int(last_result / cur_num)
                cur_num = 0
                operation = ch
        return res + last_result
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.calculate("3+2*2"))

# Use a variable to store the previous operation. By default it should be +. Each time we come across a new operation,
# we finish the previous operation and storing the result. Every time we come across + or -, we update the final result with
# it since it has to be sequential. Otherwise, we have to finish calculating the product or division first. We add a + onto the string
# to make sure it finished the previous operation, before adding the last result to the final result.

