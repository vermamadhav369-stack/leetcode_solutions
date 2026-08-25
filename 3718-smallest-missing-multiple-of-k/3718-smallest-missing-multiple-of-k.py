class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        result = set(nums)
        
        multiple = k

        while multiple in result:
            multiple += k
            
        return multiple
        