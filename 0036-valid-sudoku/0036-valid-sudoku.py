class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = {}

        for r in range(9):
            for c in range(9):

                num = board[r][c]

                if num == ".":
                    continue

                box = (r // 3, c // 3) #it is used to identify a box of any 3*3 sudoku cell and it returns a tuple.

                if box not in boxes:
                    boxes[box] = set()

                if num in rows[r]:
                    return False

                if num in cols[c]:
                    return False

                if num in boxes[box]:
                    return False

                rows[r].add(num)
                cols[c].add(num)
                boxes[box].add(num)

        return True

#TC = O(1) in fixed size but in variable input size(N*N) TC = O(N^2)
#SC = O(1) in fixed size but in variable input size(N*N) SC = O(N^2)