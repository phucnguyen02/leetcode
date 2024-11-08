# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.index = 0

    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s: return None
        head = TreeNode()
        num = 0
        mult = 1
        has_left = False

        while self.index < len(s) and s[self.index] != ")":
            if s[self.index] == "-":
                mult = -1

            elif s[self.index].isdigit():
                num = num * 10 + int(s[self.index])
            
            elif s[self.index] == "(":
                head.val = num * mult
                self.index += 1
                if not has_left:
                    has_left = True
                    head.left = self.str2tree(s)
                else:
                    head.right = self.str2tree(s)
            self.index += 1
        head.val = num * mult
        return head
    
# Do recursion while keeping track of the index. If we see a digit then add it to our number. Once we find ( then initialize our head node
# to have num as a value, and assign left, right pointers to the recursive call starting from the next index after (
# If we see ) then we break. At the end, have head be the num.