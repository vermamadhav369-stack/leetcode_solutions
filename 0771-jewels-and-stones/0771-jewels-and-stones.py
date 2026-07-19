class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        findjewels = {}
        for ch in jewels:
            findjewels[ch] = findjewels.get(ch , 0) + 1

        count = 0
        for ch in stones:
            if ch in findjewels:
                count += 1
        
        return count
        