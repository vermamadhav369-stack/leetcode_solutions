class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            nums1,nums2 =  nums2,nums1
        freq = {}
        for n in nums1:
            freq[n] = freq.get(n,0) + 1
        result = []
        for n in nums2:
            if freq.get(n,0) > 0:
                result.append(n)
                freq[n] -= 1
        return result