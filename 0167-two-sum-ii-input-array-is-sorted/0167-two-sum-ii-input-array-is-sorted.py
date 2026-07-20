class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        #In this we are using two pointers.
        low = 0
        high = len(numbers) - 1
        while low < high:
            result = numbers[low] + numbers[high]
            if result == target:
                return[low + 1 , high + 1]
            elif result < target:
                low += 1
            else:
                high -= 1
