class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count = {}
        for ch in s:
            count[ch] = count.get(ch,0) + 1

        for ch in t:
            if ch in count and count[ch] > 0:
                count[ch] -= 1
            else:
                return ch
        