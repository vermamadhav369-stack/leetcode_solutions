class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        min_index = nums.index(min(nums)) #minimum number ka index
        max_index = nums.index(max(nums)) #maximum number ka index

        case1 = max(min_index, max_index) + 1 #Dono ko front se remove karne mai kitne cost lagega

        case2 = n - min(min_index, max_index) #Dono ko back se remove karne mai kitne cost lagega

        case3 = min(min_index, max_index) + 1 + n - max(min_index, max_index) #ek ko front + ek ko back se remove karne mai kitne cost lagega.

        answer = min(case1, case2, case3)

        return answer
        