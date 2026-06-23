class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left = 0
        right = n -1
        maximum_area = 0
        while left < right:
            width = right - left
            curr_height = min(height[left],height[right])
            area = width * curr_height
            maximum_area = max(maximum_area,area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maximum_area
        