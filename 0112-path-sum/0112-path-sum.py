# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:

        def pathsum(node, target):

            if node is None:
                return False

            target -= node.val

            if target == 0 and node.left is None and node.right is None:
                return True

            return pathsum(node.left, target) or pathsum(node.right, target)

        return pathsum(root, targetSum)
        