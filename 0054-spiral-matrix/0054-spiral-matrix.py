class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix or not matrix[0]: #This checks if the matrix empty or the first row of matrix is empty.
            return []
        result = []

        #Initialize pointers for traversal
        top = 0
        left = 0
        right = len(matrix[0])-1
        bottom = len(matrix)-1

        while top <= bottom and left <= right:

            # Move left to right accross the top row.
            for i in range(left,right + 1):
                result.append(matrix[top][i])
            top += 1

            # Move top to bottom along the right column.
            for i in range(top,bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # Move right to left accross the bottom row (if still valid).
            if top <= bottom:
                for i in range(right,left - 1,-1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            # Move bottom to top along the left column (if still valid).
            if left <= right:
                for i in range(bottom, top - 1,-1):
                    result.append(matrix[i][left])
                left += 1
                
        return result
        