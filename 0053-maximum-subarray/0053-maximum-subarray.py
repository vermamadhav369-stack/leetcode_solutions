class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = 0
        maximum_sum = float("-inf")
        for i in range(n):
            total += nums[i]
            maximum_sum = max(maximum_sum,total)
            if total < 0:
                total = 0
        return maximum_sum