class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        #Leetcode Output approch
        ans = []
        depth = 0

        for ch in seq:
            if ch == "(":
                depth += 1

            ans.append(1 - depth % 2)

            if ch == ")":
                depth -= 1

        return ans
        