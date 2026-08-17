class Solution:
    def solve(self, col, board, leftrow, lowerdiagonal, upperdiagonal, n):

        if col == n:
            return 1
            
        ways = 0

        for row in range(n):
            if (
                leftrow[row] == 0
                and lowerdiagonal[row + col] == 0 
                and upperdiagonal[n - 1 + col - row] == 0 
            ):
                board[row] = board[row][:col] + "Q" + board[row][col + 1:]
                leftrow[row] = 1
                lowerdiagonal[row + col] = 1
                upperdiagonal[n - 1 + col - row] = 1

                ways += self.solve(col + 1, board, leftrow, lowerdiagonal, upperdiagonal, n)

                board[row] = board[row][:col] + "." + board[row][col + 1:]   
                leftrow[row] = 0
                lowerdiagonal[row + col] = 0
                upperdiagonal[n - 1 + col - row] = 0

        return ways
 
    def totalNQueens(self, n: int) -> int:
        board = ["." * n for _ in range(n)]
        leftrow = [0] * n
        lowerdiagonal = [0] * (2 * n - 1)
        upperdiagonal = [0] * (2 * n - 1)
        return self.solve(0, board, leftrow, lowerdiagonal, upperdiagonal, n)

        