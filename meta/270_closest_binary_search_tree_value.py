class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = root.val
        while root:
            if abs(root.val - target) < abs(closest-target):
                closest = root.val
            elif abs(root.val - target) == abs(closest-target):
                closest = min(root.val, closest)
            root = root.left if target < root.val else root.right
        return closest