class Solution:
    def hasCycle(self, head) -> bool:
        cur = head
        while cur:
            if cur.val == 10 ** 5 + 1: return True
            cur.val = 10 ** 5 + 1
            cur = cur.next
        return False

# If we pass a node, mark its value as something outside of the constraints. That way,
# if we pass it again in a cycle, we know that it's been passed because its value was not
# in the original list.

# cur = head
# while cur then
#   if cur.val == 10^5 + 1 then return true
#   cur.val = 10^5 + 1
#   cur = cur.next
# return false