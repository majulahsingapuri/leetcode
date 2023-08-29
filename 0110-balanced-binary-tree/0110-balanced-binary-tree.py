# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def search(node):
            if not node:
                return (True, 0)

            left_balanced, left = search(node.left)
            right_balanced, right = search(node.right)
            height = max(left, right) + 1

            # print(f"node: {node.val}, left_balanced: {left_balanced}, right_balanced: {right_balanced}, left: {left}, right: {right}, height: {height}")
            
            if not (left_balanced and right_balanced):
                return (False, height)
            return (abs(left - right) <= 1, height)

        return search(root)[0]