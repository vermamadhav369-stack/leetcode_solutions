class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def power(x,n):
            if n == 0:
                return 1

            half = power(x, n//2)

            if n % 2 == 0:
                return half * half
            else:
                return x * half * half

        if n < 0:
            x = 1/x
            n = -n

        return power(x , n)
        