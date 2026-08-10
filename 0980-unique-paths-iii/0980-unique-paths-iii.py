class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        i = len(grid)
        j = len(grid[0])

        #Count all non-obstacle cells
        total = 0
        for row in range(i):
            for col in range(j):
                if grid[row][col] != -1:
                    total += 1

        # Find starting position
        start_row = 0
        start_col = 0

        for row in range(i):
            for col in range(j):
                if grid[row][col] == 1:
                    start_row = row
                    start_col = col

        #Visited Matrix
        vis = [[0 for _ in range(j)] for _ in range(i)]

        def maze(row, col, count):

            #Reached ending cell
            if grid[row][col] == 2:
                if count == total:
                    return 1
                return 0

            ways = 0

            #Marked current cell
            vis[row][col] = 1

            #Downward
            if row + 1 < i and not vis[row + 1][col] and grid[row + 1][col] != -1:
                ways += maze(row + 1, col, count + 1)

            #Left
            if col - 1 >= 0 and not vis[row][col - 1] and grid[row][col - 1] != -1:   
                ways += maze(row, col - 1, count + 1)
               
            #Right
            if col + 1 < j and not vis[row][col + 1] and grid[row][col + 1] != -1:
                ways += maze(row, col + 1, count + 1)
                
            #Upward
            if row - 1 >= 0 and not vis[row - 1][col] and grid[row - 1][col] != -1: 
                ways += maze(row - 1, col, count + 1)

            #Backtrack
            vis[row][col] = 0

            return ways

        return maze(start_row, start_col, 1)
        