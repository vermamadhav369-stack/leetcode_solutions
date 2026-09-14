# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def balanced_height(node):

            if node is None:
                return 0

            l_h = balanced_height(node.left)
            if l_h == -1:
                return -1

            r_h = balanced_height(node.right)
            if r_h == -1:
                return -1
            
            if abs(l_h - r_h) > 1:
                return -1

            return 1 + max(l_h, r_h)

        x = balanced_height(root)
        if x == -1:
            return False
        return True
        