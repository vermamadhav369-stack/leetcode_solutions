class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in range(len(nums)-2):
            # Skip duplicate first elements
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1

            while j < k:
                curr_sum = nums[i] + nums[j] + nums[k]
                if curr_sum == 0:
                    result.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    # Skip duplicate left values
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    # Skip duplicate right values
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif curr_sum < 0:
                    j += 1
                else:
                    k -= 1
        return result   