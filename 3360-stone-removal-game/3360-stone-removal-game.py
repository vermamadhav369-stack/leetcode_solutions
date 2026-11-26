class Solution:
    def canAliceWin(self, n: int) -> bool:
        stones = n
        remove = 10
        turn = 0

        while stones >= remove and remove > 0:
            stones -= remove
            remove -= 1
            turn += 1

        if turn % 2 == 0:
            return False
        else:
            return True