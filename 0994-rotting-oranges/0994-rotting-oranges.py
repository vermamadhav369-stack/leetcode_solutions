class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        grid_copy = deepcopy(grid)

        fresh_cnt = 0
        queue = deque()

        #Here we are storing all the co-ordinates of Rotten oranges and counting all the fresh oranges.
        for r in range(rows):
            for c in range(cols):
                if grid_copy[r][c] == 2:
                    queue.append((r,c))
                elif grid_copy[r][c] == 1:
                    fresh_cnt += 1

        minutes = 0
        while len(queue) != 0 and fresh_cnt > 0:
            minutes += 1
            total_rotten = len(queue)

            for _ in range(total_rotten):
                i, j = queue.popleft()

                for di, dj in [(1, 0), (-1, 0), (0, -1), (0, 1)]: #For checking if we found any rotten oranges in all four directions.
                    new_i, new_j = i + di, j + dj

                    if new_i < 0 or new_i == rows or new_j < 0 or new_j == cols: #For checking-> if we go outside the grid then continue.
                        continue
                    
                    if grid_copy[new_i][new_j] == 2 or grid_copy[new_i][new_j] == 0: #if we found any rotten oranges or empty space then continue.
                        continue

                    fresh_cnt -= 1 #agar hame koi fresh orange milta to fresh_count ko 1 se kam kardo
                    grid_copy[new_i][new_j] = 2 # Aur grid mai uss fresh orange ko rotten(2) kardo
                    queue.append((new_i, new_j)) #Aur uss new rotten orange ki position ko queue mai daal do

        if fresh_cnt > 0:
            return -1
        return minutes
                