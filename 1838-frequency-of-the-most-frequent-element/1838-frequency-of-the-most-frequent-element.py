class Solution:
    def maxFrequency(self, arr, k):
        
        arr.sort()
        left = 0
        window_sum = 0
        ans = 1
        
        for right in range(len(arr)):
            window_sum += arr[right]
            
            increments = arr[right] * (right-left+1) - window_sum
            
            while increments > k:
                window_sum -= arr[left]
                left += 1
                increments = arr[right] * (right-left+1) - window_sum
                
            ans = max(ans, right - left + 1)
            
        return ans
        