class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:

        mini = min(nums)
        maxi = max(nums)

        ans = set(nums)
        result = []

        for i in range(mini + 1, maxi):
            if i not in ans:
                result.append(i)

        return result
        