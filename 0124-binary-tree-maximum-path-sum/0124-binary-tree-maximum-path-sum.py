# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi = float("-inf")

        def path_sum(node):
            nonlocal maxi

            if node is None:
                return 0

            left_sum = path_sum(node.left)
            if left_sum < 0:
                left_sum = 0

            right_sum = path_sum(node.right)
            if right_sum < 0:
                right_sum = 0

            maxi = max(maxi, left_sum + node.val + right_sum)
            return node.val + max(left_sum, right_sum)

        path_sum(root)
        return maxi
        