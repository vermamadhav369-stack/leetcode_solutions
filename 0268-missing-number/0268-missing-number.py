class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) 
        excepted_sum = n * (n+1) // 2
        actual_sum = 0
        for num in nums:
            actual_sum += num
        return excepted_sum - actual_sum
        