class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 1:
            last_bit = n & 1
            n >>= 1
            new_last_bit = n & 1
            if last_bit == new_last_bit:
                return False

        return True