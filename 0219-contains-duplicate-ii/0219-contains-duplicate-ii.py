class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        result = {}
        for i in range(n):
            if nums[i] in result:
                distance = i - result[nums[i]]
                if distance <= k:
                    return True
            result[nums[i]] = i
        return False
        