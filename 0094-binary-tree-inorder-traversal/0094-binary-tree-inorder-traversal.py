# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def in_order(node):
            if node is None:
                return

            in_order(node.left)
            result.append(node.val)
            in_order(node.right)

        in_order(root)
        return result
        