class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(row, col):

            #Base condition
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] == 0:
                return 0

            gold = grid[row][col] #current cell ka gold save karo
            grid[row][col] = 0    #Mark Visited

            #Calculate Gold for all 4 directions
            down = dfs(row + 1, col)
            left = dfs(row, col - 1)
            right = dfs(row, col + 1)
            up = dfs(row - 1, col)

            grid[row][col] = gold #Backtracking : original value restore

            current_gold = max(down, left, right, up) #Best direction

            gold += current_gold 

            return gold

        ans = 0
        #Har gold cell se DFS start karne ke liye 
        for row in range(m):
            for col in range(n):
                if grid[row][col] != 0:
                    ans = max(ans, dfs(row, col))

        return ans
        