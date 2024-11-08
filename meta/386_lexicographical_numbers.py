class Solution:
    def lexicalOrder(self, n: int):
        res = []
        def dfs(cur_num):
            nonlocal n
            if cur_num > n:
                return

            res.append(cur_num)
            for i in range(10):
                next_num = cur_num * 10 + i
                if next_num <= n:
                    dfs(next_num)
                else:
                    break

        for i in range(1, 10):
            dfs(i)
        return res 
    
# Do DFS on every digit, stop if the current num exceeds n since every digit after would exceed n as well