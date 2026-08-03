class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        def solve(index, subset):
            if index == len(nums):
                result.append(subset.copy())
                return

            #Include current element
            subset.append(nums[index])
            solve(index + 1, subset)
            subset.pop()

            #Skip Duplicates before excluding
            nextindex = index
            while nextindex + 1 < len(nums) and nums[nextindex] == nums[nextindex + 1]:
                nextindex += 1

            #Exclude current element and all its Duplicates
            solve(nextindex + 1, subset)

        solve(0, [])
        return result
        