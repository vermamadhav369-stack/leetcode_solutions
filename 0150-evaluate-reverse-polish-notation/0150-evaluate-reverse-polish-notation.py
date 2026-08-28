class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for x in tokens:
            if x not in ["+","-","*","/"]:
                stack.append(int(x))
            
            elif x == "+":
                operand1 = stack.pop()
                operand2 = stack.pop()
                stack.append(operand2 + operand1)

            elif x == "-":
                operand1 = stack.pop()
                operand2 = stack.pop()
                stack.append(operand2 - operand1)

            elif x == "*":
                operand1 = stack.pop()
                operand2 = stack.pop()
                stack.append(operand2 * operand1)

            elif x == "/":
                operand1 = stack.pop()
                operand2 = stack.pop()
                stack.append(int(operand2 / operand1))

        return stack[-1]
        