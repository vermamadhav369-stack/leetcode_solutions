class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        n = len(nums)
        result = {}
        for i in range(n):
            if nums[i] in result:
                distance = i - result[nums[i]]
                if distance <= k:
                    return True
            result[nums[i]] = i
        return False