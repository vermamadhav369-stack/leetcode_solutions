class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        total = 0
        maximum_sum = float("-inf")
        for i in range(len(nums)):
            total += nums[i]
            maximum_sum = max(maximum_sum, total)
            if total < 0:
                total = 0

        return maximum_sum