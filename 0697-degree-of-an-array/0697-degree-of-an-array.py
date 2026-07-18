class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        first = {}
        last = {}
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i],0) + 1

            if nums[i] not in first:
                first[nums[i]] = i
            last[nums[i]] = i

        degree = max(count.values())
        mini = float("inf")

        for num in count:
            if count[num] == degree:
                length = last[num] - first[num] + 1
                mini = min(mini,length)
        return mini        