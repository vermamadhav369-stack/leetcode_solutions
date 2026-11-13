class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        result = {}
        for i in range(len(nums)):
            result[nums[i]] = result.get(nums[i] , 0) + 1

        ans = []
        for j in range(k):
            great = max(result, key= result.get) #key= result.get -> dictionary ki values(frequencies) ke according maximum key find krega.

            ans.append(great)
            del result[great]

        return ans

        #TC = O(N+K*M) => O(N^2)[worst case]
        #SC = O(M+K) => since K <= M => O(M) => O(N)(worst case)