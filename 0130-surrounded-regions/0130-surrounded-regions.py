class Solution:
    def dfs(self, r, c, visited, rows, cols, board):
        if r < 0 or r == rows or c < 0 or c == cols:
            return

        if visited[r][c] == 1:
            return

        if board[r][c] == "X":
            return

        visited[r][c] = 1
        self.dfs(r + 1, c, visited, rows, cols, board) #Down
        self.dfs(r - 1, c, visited, rows, cols, board) #Top
        self.dfs(r, c + 1, visited, rows, cols, board) #Right
        self.dfs(r, c - 1, visited, rows, cols, board) #Left

    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        #Upper Row
        r, c = 0, 0
        for c in range(cols):
            if board[r][c] == "O":
                if visited[r][c] == 0:
                    self.dfs(r, c, visited, rows, cols, board)

        #Last row
        r, c = rows-1, 0
        for c in range(cols):
            if board[r][c] == "O":
                if visited[r][c] == 0:
                    self.dfs(r, c, visited, rows, cols, board)

        #First column
        r, c = 0, 0
        for r in range(rows):
            if board[r][c] == "O":
                if visited[r][c] == 0:
                    self.dfs(r, c, visited, rows, cols, board)

        #Last column
        r, c = 0, cols-1
        for r in range(rows):
            if board[r][c] == "O":
                if visited[r][c] == 0:
                    self.dfs(r, c, visited, rows, cols, board)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and visited[r][c] == 0:
                    board[r][c] = "X"