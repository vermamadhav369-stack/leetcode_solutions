class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        count = 0
        maxi = 0
        i = 0
        for i in range(n):
            if nums[i] == 1:
                count += 1
            else:
                maxi = max(maxi,count)
                count = 0
        return max(maxi,count)

            

                