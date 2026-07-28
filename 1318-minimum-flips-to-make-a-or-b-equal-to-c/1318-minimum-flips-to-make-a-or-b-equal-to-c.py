class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        ans = 0
        for i in range(32):
            a_bit = (a>>i) & 1
            b_bit = (b>>i) & 1
            c_bit = (c>>i) & 1

            if c_bit:
                if a_bit == 0 and b_bit == 0:
                    ans+=1

            else:
                ans += a_bit + b_bit

        return ans
        