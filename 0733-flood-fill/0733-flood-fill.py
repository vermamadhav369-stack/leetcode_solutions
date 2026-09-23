class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        if image[sr][sc] == color:
            return image

        image_copy  = deepcopy(image)
        rows = len(image_copy)
        cols = len(image_copy[0])
        initial_color = image_copy[sr][sc]

        def dfs(r, c, new_color, image_copy, initial_color, rows, cols):

            if r < 0 or r == rows or c < 0 or c == cols: #If we go outside the image then return
                return

            if image_copy[r][c] != initial_color:
                return

            if image_copy[r][c] == new_color:
                return

            image_copy[r][c] = new_color

            dfs(r - 1, c, new_color, image_copy, initial_color, rows, cols) #TOP
            dfs(r + 1, c, new_color, image_copy, initial_color, rows, cols) #BOTTOM
            dfs(r, c - 1, new_color, image_copy, initial_color, rows, cols) #LEFT
            dfs(r, c + 1, new_color, image_copy, initial_color, rows, cols) #RIGHT

        dfs(sr, sc, color, image_copy, initial_color, rows, cols)
        return image_copy
