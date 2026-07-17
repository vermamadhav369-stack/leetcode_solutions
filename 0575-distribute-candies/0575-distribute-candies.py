class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        half = len(candyType) // 2
        check = set(candyType)
        uniqueType = len(check)
        uniqueType = min(half , uniqueType)
        return uniqueType
        