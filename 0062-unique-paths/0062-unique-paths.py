class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1] * n for _ in range(m)]
        
        def answer(row, col):
            if row == m - 1 and col == n - 1:
                return 1

            if dp[row][col] != -1:
                return dp[row][col]

            ways = 0
            #Down
            if row + 1 < m:
                ways += answer(row + 1, col)

            #Right
            if col + 1 < n:
                ways += answer(row, col + 1)

            dp[row][col] = ways

            return ways
        return answer(0, 0)
    