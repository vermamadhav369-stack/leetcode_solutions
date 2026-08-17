class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def solve(start, subset):

            if len(subset) == k:
                result.append(subset[:])
                return

            for i in range(start, n + 1):
                subset.append(i)
                solve(i + 1, subset)
                subset.pop()

        solve(1, [])
        return result
        