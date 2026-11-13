class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        #optimal solution

        result = {}
        for n in strs:
            count = [0] * 26

            for ch in n:
                count[ord(ch) - ord('a')] += 1

            key = tuple(count)

            if key not in result:
                result[key] = []

            result[key].append(n)

        return list(result.values())        
