class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if k == 1:
            count = {}
            for x in nums:
                count[x] = count.get(x, 0) + 1

            ans = -1
            for x in count:
                if count[x] == 1:
                    ans = max(ans, x)
            return ans

        if k == len(nums):
            return max(nums)

        ans = -1
        if nums.count(nums[0]) == 1:
            ans = max(ans, nums[0])

        if nums.count(nums[-1]) == 1:
            ans = max(ans, nums[-1])

        return ans
