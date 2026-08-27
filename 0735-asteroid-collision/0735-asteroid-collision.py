class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        stack = []

        for i in range(n):
            ch = asteroids[i]

            #if the number is positive add it to stack.
            if ch > 0:
                stack.append(ch)
            
            #if the stack is not empty and the last element is positive in stack and the last element is smaller than the current element remove the last element from stack.
            else:
                while stack and stack[-1] > 0 and stack[-1] < abs(ch):
                    stack.pop()

                #if the stack is not empty and the last element in stack is equal to current element, remove the last element from stack.
                if stack and stack[-1] == abs(ch):
                    stack.pop()

                #if the stack is empty or the last element in stack is negative, add the current number in stack.
                elif len(stack) == 0 or stack[-1] < 0:
                    stack.append(ch)

        return stack
