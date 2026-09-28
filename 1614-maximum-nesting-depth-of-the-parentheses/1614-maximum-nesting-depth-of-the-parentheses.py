class Solution:
    def maxDepth(self, s: str) -> int:

        curr_depth = 0
        max_depth = 0

        for ch in s:
            if ch == "(":
                curr_depth += 1
                max_depth = max(curr_depth, max_depth)

            elif ch == ")":
                curr_depth -= 1

        return max_depth
        