class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        count = 0

        def dfs(i, j):

            #Boundarycheck
            if i < 0 or i >= row or j < 0 or j >= col:
                return

            #Water
            if grid[i][j] == "0":
                return

            #Mark as visited
            grid[i][j] = "0"

            #Top
            dfs(i - 1, j)

            #Bottom
            dfs(i + 1, j)

            #Left
            dfs(i, j - 1)

            #Right 
            dfs(i, j + 1)

        #Traverse the whole grid
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)

        return count
        

        