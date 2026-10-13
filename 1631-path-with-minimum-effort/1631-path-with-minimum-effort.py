class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])

        effort_arr = [[float("inf") for _ in range(cols)] for _ in range(rows)]
        effort_arr[0][0] = 0

        priority_queue = [[0, 0, 0]]

        while len(priority_queue) != 0:
            eff, r, c = heapq.heappop(priority_queue)
            if r == rows - 1 and c == cols - 1:
                return eff

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                new_r, new_c = r + dr, c + dc

                if new_r < 0 or new_r == rows or new_c < 0 or new_c == cols:
                    continue

                new_effort = max(eff, abs(heights[new_r][new_c] - heights[r][c]))

                if new_effort < effort_arr[new_r][new_c]:
                    effort_arr[new_r][new_c] = new_effort
                    heapq.heappush(priority_queue,[new_effort, new_r, new_c])

            