# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        ans = []

        def rightview(node, level):

            if node is None:
                return

            if len(ans) == level:
                ans.append(node.val)

            if node.right:
                rightview(node.right, level + 1)

            if node.left:
                rightview(node.left, level + 1)

        rightview(root, 0)
        return ans

        