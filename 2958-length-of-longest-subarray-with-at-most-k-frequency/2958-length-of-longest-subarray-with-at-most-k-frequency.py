class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
         
        result = {}
        l = 0
        length = 0

        for r in range(len(nums)):
            result[nums[r]] = result.get(nums[r] , 0) + 1

            while result[nums[r]] > k:
                result[nums[l]] -= 1
                l += 1

            current_length = r - l + 1
            length = max(current_length, length)

        return length
        