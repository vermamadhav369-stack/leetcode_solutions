class Solution:
    def longestPalindrome(self, s: str) -> int:

        result = {}
        count = 0
        odd = 0

        #Count Frequency of each character.
        for ch in s:
            result[ch] = result.get(ch, 0) + 1

        #Calculate Plaindrome length.
        for ch in result:

            if result[ch] % 2 == 0:
                count += result[ch]
            else:
                count += result[ch] - 1
                odd = 1

        #One odd character can be place in the center.
        if odd == 1:
            count += 1

        return count
        