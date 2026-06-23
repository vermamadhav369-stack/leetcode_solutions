class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        dict = {}
        for i in range(n):
            answer = target-nums[i]
            if answer in dict:
                return [dict[answer],i]
            dict[nums[i]] = i
