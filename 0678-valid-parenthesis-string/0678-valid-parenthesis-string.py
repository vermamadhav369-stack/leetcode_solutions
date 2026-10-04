class Solution:
    def checkValidString(self, s: str) -> bool:
        #Greedy 

        low = 0 #minimum possible unmached (
        high = 0 #maximum possible unmached (

        for ch in s:
            if ch == "(":
                low += 1
                high += 1

            elif ch == ")":
                low -= 1
                high -= 1

            else: # (*) ke case
                low -= 1 #minimum ke liye * ko closing [)] maan lo
                high += 1 #maximum ke liye * ko opening [(] maan lo

            low = max(low, 0) #low ko 0 se neeche nehi jane dena kyuki unmatched opening[(] brackets ki count negative nehi hosakti [Ex- "*)"]. 

            if high < 0: #eska matlab hai ki * ko best possible way mai use karne pe bhi hamare pass ek bhi opening [(] nehi bacha
                return False

        return low == 0

        