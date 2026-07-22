class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        k = len(nums) - 1
        while i <= k:
            if nums[i] == val:
                nums[i],nums[k] = nums[k],nums[i]
                k -= 1
            else:
                i += 1

        return k + 1