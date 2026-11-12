class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        result = {}

        for n in nums:
            if n in result:
                return True

            result[n] = 1

        return False