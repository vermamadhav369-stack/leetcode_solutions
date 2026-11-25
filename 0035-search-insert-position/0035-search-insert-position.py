class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        position = len(nums)
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] >= target:
                position = mid
                right = mid - 1
            else:
                left = mid + 1        
        return position 