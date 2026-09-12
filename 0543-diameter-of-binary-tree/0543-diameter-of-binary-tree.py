# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def max_height(node):
            nonlocal diameter #nonlocal is a keyword used inside a nested function to tell python:"use the variable from the outer function instead of creating a new local variable."
            if node == None:
                return 0

            left_height = max_height(node.left)
            right_height = max_height(node.right)
            diameter = max(diameter, left_height + right_height)
            return 1 + max(left_height, right_height)

        max_height(root)
        return diameter
        