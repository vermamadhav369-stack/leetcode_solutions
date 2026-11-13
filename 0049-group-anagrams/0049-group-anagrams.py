class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = {}

        for n in strs:
            ch = "".join(sorted(n))
            if ch not in result:
                result[ch] = []

            result[ch].append(n)

        return list(result.values())
