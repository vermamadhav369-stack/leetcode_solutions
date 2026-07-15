class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        count = {}
        for ch in ransomNote:
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1

        for ch in magazine:
            if ch in count:
                count[ch] -= 1
        
        for value in count.values():
            if value> 0:
                return False
                
        return True
