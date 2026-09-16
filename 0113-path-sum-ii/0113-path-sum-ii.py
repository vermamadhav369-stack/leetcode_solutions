# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:

        path = []
        ans = []

        def dfs(node, curr_sum):

            if node is None:
                return

            path.append(node.val)
            curr_sum += node.val
            
            #Check leaf node
            if node.left is None and node.right is None:
                if curr_sum == targetSum:
                    ans.append(path.copy())

            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)

            #Backtrack
            path.pop()

        dfs(root, 0)
        return ans
        