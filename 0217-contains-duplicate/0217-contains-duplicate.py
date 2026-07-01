class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        result = {}
        for n in nums:
            if n in result:
                return True
            result[n] = 1
        return False
        