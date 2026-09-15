# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: #(SELF Solution)
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        ans = []
        result = {}
        queue = deque()

        queue.append((root, 0))

        while queue:
            e, line = queue.popleft()

            result[line] = e.val

            if e.left:
                queue.append((e.left, line + 1))

            if e.right:
                queue.append((e.right, line + 1))

        for value in sorted(result.items()): 
            ans.append(value[1])

        return ans