class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for x in operations:
            #if x is a integer add in record.
            if x not in ["C", "D", "+"]:
                record.append(int(x))

            #Record a new score that is the double of the previous score.
            elif x == "D":
                record.append(record[-1] * 2)

            #Invalidate the previous score, removing it from the record.
            elif x == "C":
                record.pop()

            #Record a new score that is the sum of the previous two scores.
            elif x == "+":
                record.append(record[-1] + record[-2])
        
        #Return the sum of all the scores on the record after applying all the operations.
        return sum(record)
        