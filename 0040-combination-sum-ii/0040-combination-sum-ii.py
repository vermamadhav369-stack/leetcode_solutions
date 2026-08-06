class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def solve(index, total, subset):

            if total == target:
                result.append(subset.copy())
                return

            elif total > target:
                return

            if index == len(candidates):
                return

            subset.append(candidates[index])
            solve(index + 1, total + candidates[index], subset)

            subset.pop()

            nextindex = index
            while nextindex + 1 < len(candidates) and candidates[nextindex] == candidates[nextindex + 1]:
                 nextindex += 1
            solve(nextindex + 1, total, subset)

        solve(0, 0, [])
        return result




        