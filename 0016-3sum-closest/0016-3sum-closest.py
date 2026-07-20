class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                curr_sum = nums[i] + nums[j] + nums[k]
                if abs(curr_sum - target) < abs(closest - target):
                    closest = curr_sum
                
                if curr_sum == target:
                    return curr_sum
                elif curr_sum < target:
                    j += 1
                else:
                    k -= 1
        
        return closest
        