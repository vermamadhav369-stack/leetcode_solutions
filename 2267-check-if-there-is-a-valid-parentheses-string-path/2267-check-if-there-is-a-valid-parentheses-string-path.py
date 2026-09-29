class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])

        #path length must be even
        if (rows + cols - 1) % 2 != 0:
            return False
        
        memo = {}

        def dfs(r, c, balance):

            #out of bounds
            if r == rows or c == cols:
                return False

            #update balance
            if grid[r][c] == "(":
                balance += 1
            else:
                balance -= 1

            #For invalid parentheses
            if balance < 0:
                return False

            #kya hum Destination(last row ke last coloum) pe pauch gaye kya
            if r == rows - 1 and c == cols - 1:
                return balance == 0

            #Already calculated path hai to memo(dictionary) mai uss path ki value return karvado
            if (r, c, balance) in memo:
                return memo[(r, c, balance)]

            #Move down or right
            down = dfs(r + 1, c, balance)
            right = dfs(r, c + 1, balance)

            result = down or right #maan lo ki hame kisi path se True mila to vo result mai save hoga aur phir hum uss result ko (key,value) ke pair mai memorization vali dictionary mai save kardenge
            #Store result in memorization
            memo[(r, c, balance)] = result #eska matlab hai ki current (r, c, balance) ko key banao or result ko uski value ke roop mai save karo

            return result

        return dfs(0, 0, 0)

        