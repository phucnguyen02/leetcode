class Solution:
    def simplifyPath(self, path: str) -> str:
        if path == "/": return "/"
        directories = path.split("/")
        stack = []
        for dir in directories:
            if dir == "..":
                if stack: stack.pop()
            elif dir != '.' and dir != '':
                stack.append(dir)
        return '/' + '/'.join(stack)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.simplifyPath("/home//foo/"))
    print(sol.simplifyPath("/home/user/Documents/../Pictures"))
    print(sol.simplifyPath("/../"))
    print(sol.simplifyPath("/.../a/../b/c/../d/./"))


# Split the path into all of the possible directories separated by /
# For each non .. or . directory, we add it into a stack. If we encounter .., we pop the stack if it has an element.
# After that, join all of the elements of the stack with / and prepend / to it.