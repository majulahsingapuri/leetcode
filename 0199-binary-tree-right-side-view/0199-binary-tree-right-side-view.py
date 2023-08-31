# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        memo = []

        def search(node, level = 0):
            if not node:
                return
            nonlocal memo
            try:
                memo[level].append(node.val)
            except:
                memo.append([node.val])

            search(node.left, level + 1)
            search(node.right, level + 1)

        search(root)
        for i, level in enumerate(memo):
            memo[i] = level[-1]
        return memo