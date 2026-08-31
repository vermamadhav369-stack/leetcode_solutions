class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        left = 0
        right = 0
        count = {}
        max_freq = 0
        longest_substring = 0

        while right < n:
            count[s[right]] = count.get(s[right], 0) + 1

            max_freq = max(max_freq, count[s[right]])

            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            longest_substring = max(longest_substring, right - left + 1)
            right += 1
            
        return longest_substring 
        