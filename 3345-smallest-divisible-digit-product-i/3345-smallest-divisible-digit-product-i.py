class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            if self.helper(n) % t == 0:
                return n
            n += 1

    def helper(self, num):
        product = 1
        while num > 0:
            ld = num % 10
            product *= ld
            num = num // 10
        return product
        