# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def search(node, curMax = None):
            if not node:
                return 0
            increment = 1 if curMax is None or node.val >= curMax else 0
            newMax = max(node.val, curMax) if curMax else node.val
            return search(node.left, newMax) + search(node.right, newMax) + increment

        return search(root)