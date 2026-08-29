class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        number = 0
        current = ""

        for ch in s:
            if ch.isdigit():
                number = number * 10 + int(ch)

            elif ch == "[":
                stack.append((current, number))
                current = ""
                number = 0

            elif ch == "]":
                prev_current, repeat_number = stack.pop()
                current = prev_current + current * repeat_number

            else:
                current += ch

        return current      