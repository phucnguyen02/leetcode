class Solution:
    def __init__(self):
        self.index = 0

    def parse(self, expression):
        t_count = f_count = 0
        while self.index < len(expression) and expression[self.index] != ")":
            if expression[self.index] in "&!|":
                operation = expression[self.index]
                self.index += 1
                inner_t, inner_f = self.parse(expression)
                if operation == "&":
                    if inner_f > 0: f_count += 1
                    else: t_count += 1
                elif operation == "!":
                    if inner_f > 0: t_count += 1
                    else: f_count += 1
                else:
                    if inner_t > 0: t_count += 1
                    else: f_count += 1
            elif expression[self.index] == "t":
                t_count += 1
            elif expression[self.index] == "f":
                f_count += 1

            self.index += 1
        return [t_count, f_count]
    def parseBoolExpr(self, expression: str) -> bool:
        if expression == "t" or expression == "f":
            return True if expression == "t" else False
        inner_t, inner_f = self.parse(expression)
        return True if inner_t else False
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.parseBoolExpr("&(|(f))"))
    sol = Solution()
    print(sol.parseBoolExpr("|(f,f,f,t)"))
    sol = Solution()
    print(sol.parseBoolExpr("!(&(f,t))"))

# When evaluating an expression, keep track of the number of ts and fs within that expression, so that we may update their number in the outer expression.
# If our operation is & then we evaluate to true if f_count == 0 and false otherwise, for instance