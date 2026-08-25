class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        result = {}

        #Find next greater element in nums2.
        for num in nums2:
            while stack and stack[-1] < num:
                result[stack[-1]] = num
                stack.pop()
            stack.append(num)

        #Remaining elements have no greater element.
        while stack:
            result[stack[-1]] = -1
            stack.pop()

        #Create answer for nums1.
        answer = []
        for num in nums1:
            answer.append(result[num])

        return answer
        