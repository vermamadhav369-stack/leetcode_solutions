class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = 0
        total = float("inf")
        curr_sum = 0

        while r < n:
            curr_sum += nums[r]
            r += 1

            while curr_sum >= target:
                total = min(total, r - l)

                curr_sum -= nums[l]
                l += 1

        if total == float("inf"):
            return 0
            
        return total
