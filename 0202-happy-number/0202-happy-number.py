class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #Solved using extraction of digits.
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            total = 0
            while n > 0:
                last_digit = n % 10
                total = total + (last_digit * last_digit)
                n = n // 10
            n = total
        return True 