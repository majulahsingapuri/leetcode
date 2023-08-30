# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(p: TreeNode, q: TreeNode) -> bool:
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
            else:
                return False

        def find(node):
            if not node:
                return False
            check = False
            if node.val == subRoot.val:
                check = isSameTree(node, subRoot)
            return check or find(node.left) or find(node.right)
            
        
        return find(root)