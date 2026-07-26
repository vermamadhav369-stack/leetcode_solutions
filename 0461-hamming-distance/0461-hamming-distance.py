class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        ans = x ^ y
        count = 0
        while ans > 0:
            if ans & 1:
                count += 1
            ans >>= 1
        return count

        