class Solution:
    def simplifyPath(self, path, change) -> str:
        stack = []
        directories = path.split("/")
        for dir in directories:
            if dir != "":
                stack.append(dir)

        directories = change.split("/")

        for dir in directories:
            if dir == "" or dir == ".": continue

            if dir == "..":
                if stack:
                    stack.pop()
            
            else:
                stack.append(dir)

        return "/" + "/".join(stack)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.simplifyPath("/", "/facebook"))
    print(sol.simplifyPath("/facebook/anin", "../abc/def"))
    print(sol.simplifyPath("/facebook/instagram", "../../../."))