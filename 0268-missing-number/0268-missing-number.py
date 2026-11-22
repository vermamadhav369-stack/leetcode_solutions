class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)

        expected_sum = n * (n + 1) // 2
        actual_sum = 0

        for num in nums:
            actual_sum += num

        return expected_sum - actual_sum