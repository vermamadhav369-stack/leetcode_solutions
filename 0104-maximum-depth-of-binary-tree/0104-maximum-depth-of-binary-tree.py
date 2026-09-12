# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: #Recursion
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def max_height(node):
            if node == None:
                return 0

            left_height = max_height(node.left)
            right_height = max_height(node.right)
            return 1 + max(left_height, right_height)

        return max_height(root)
 