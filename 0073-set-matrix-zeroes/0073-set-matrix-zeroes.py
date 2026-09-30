class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        row_track = [0 for _ in range(rows)]
        cols_track = [0 for _ in range(cols)]

        for r in range(rows):
            for c in range(cols):

                if matrix[r][c] == 0:
                    row_track[r] = -1
                    cols_track[c] = -1

        for r in range(rows):
            for c in range(cols):

                if row_track[r] == -1 or cols_track[c] == -1:
                    matrix[r][c] = 0
        