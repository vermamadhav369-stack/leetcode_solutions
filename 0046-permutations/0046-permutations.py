class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def solve(subset):

            if len(subset) == len(nums):
                result.append(subset[:])
                return

            for i in range(len(nums)):
                if nums[i] in subset:
                    continue

                subset.append(nums[i])
                solve(subset)
                subset.pop()
        solve([])
        return result