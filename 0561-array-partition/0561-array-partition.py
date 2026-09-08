class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        maximum_sum = 0
        nums.sort()

        for i in range(0, n, 2):
            maximum_sum += nums[i]

        return maximum_sum
        