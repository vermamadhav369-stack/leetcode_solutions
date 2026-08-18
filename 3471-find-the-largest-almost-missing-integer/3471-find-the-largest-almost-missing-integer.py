class Solution: 
    def largestInteger(self, nums: List[int], k: int) -> int:
        result = []
        subarray = []
        for i in range(len(nums)):
            subarray.append(nums[i])
            if len(subarray) == k:
                result.append(subarray[:])
                subarray.pop(0)

        count = {}
        for subarray in result:
            for x in set(subarray):
                count[x] = count.get(x , 0) + 1

        ans = -1
        for x in count:
            if count[x] == 1:
                ans = max(ans, x)

        return ans
        