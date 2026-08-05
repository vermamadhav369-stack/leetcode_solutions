class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        numbers = [""] *(n * 2)
        result = []

        def solve(index,total,numbers):

            if index == len(numbers):
                if total == 0:
                    result.append("".join(numbers))
                return

            if total > len(numbers) // 2:
                return
            elif total < 0:
                return

            numbers[index] = "("      
            solve(index + 1, total + 1, numbers)

            numbers[index] = ")"    
            solve(index + 1, total - 1, numbers)

        solve(0, 0, numbers)
        return(result)
        