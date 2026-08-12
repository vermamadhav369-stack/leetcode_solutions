class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m = len(obstacleGrid) #Row
        n = len(obstacleGrid[0]) #Column
        dp = [[-1] * n for _ in range(m)]

        def answer(row, col):

            if obstacleGrid[row][col] == 1: #Obstacle
                return 0

            if row == m - 1 and col == n - 1: #Destination
                return 1

            if dp[row][col] != -1: #For Memorization
                return dp[row][col]

            ways = 0

            #Down
            if row + 1 < m and obstacleGrid[row + 1][col] == 0:
                ways += answer(row + 1, col)

            #Right
            if col + 1 < n and obstacleGrid[row][col + 1] == 0:
                ways += answer(row, col + 1)

            dp[row][col] = ways

            return ways
        return answer(0, 0)

        