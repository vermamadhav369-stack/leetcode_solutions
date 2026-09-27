class Solution:
    def bfs(self, i, j, visited, grid):
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        queue.append((i, j))
        visited[i][j] = 1

        while len(queue) != 0:
            x, y = queue.popleft()

            for dx, dy in[(1, 0),(-1, 0),(0, 1),(0, -1)]:
                new_x, new_y = x + dx, y + dy

                if new_x < 0 or new_x == rows or new_y < 0 or new_y == cols:
                    continue
                
                if visited[new_x][new_y] == 1:
                    continue

                if grid[new_x][new_y] == "0":
                    continue

                visited[new_x][new_y] = 1
                queue.append((new_x, new_y))                


    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        rows = len(grid)
        cols = len(grid[0])

        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if visited[r][c] == 0 and grid[r][c] == "1":
                    count += 1
                    self.bfs(r, c, visited, grid)

        return count
