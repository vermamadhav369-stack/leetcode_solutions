class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:

        if grid[0][0] == 1:
            return -1
        
        rows = len(grid)
        cols = len(grid[0])

        distance = [[float("inf") for _ in range(cols)] for _ in range(rows)]
        distance[0][0] = 1

        queue = deque()
        queue.append([1,0,0])

        while len(queue) != 0:
            dist, r, c = queue.popleft()
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1), (-1,-1), (-1,1), (1,-1), (1,1)]:
                new_r, new_c = r + dr, c + dc

                if new_r < 0 or new_r == rows or new_c < 0 or new_c == cols:
                    continue
                if grid[new_r][new_c] == 1:
                    continue

                new_dist = dist + 1

                if new_dist < distance[new_r][new_c]:
                    if new_r == rows - 1 and new_c == cols - 1:
                        return new_dist

                    distance[new_r][new_c] = new_dist
                    queue.append([new_dist,new_r,new_c])

        if distance[rows-1][cols-1] == float("inf"):
            return -1

        return distance[rows-1][cols-1]