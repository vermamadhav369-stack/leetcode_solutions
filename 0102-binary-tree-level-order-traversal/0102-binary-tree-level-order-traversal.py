# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        result = []

        def bfs(node):
            if not node:
                return

            queue = deque([])
            queue.append(node)

            while len(queue) != 0:
                level = []
                level_size = len(queue)
                
                for _ in range(level_size):
                    e = queue.popleft()
                    level.append(e.val)

                    if e.left:
                        queue.append(e.left)

                    if e.right:
                        queue.append(e.right)

                result.append(level)

        bfs(root)
        return result
                        