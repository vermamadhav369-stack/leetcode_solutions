class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        result = {}
        for i in range(len(nums)):

            comp = target - nums[i]
            if comp in result:
                return [result[comp],i]

            result[nums[i]] = i