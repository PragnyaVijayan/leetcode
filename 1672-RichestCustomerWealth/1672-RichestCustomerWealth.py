# Last updated: 9/9/2025, 9:18:48 PM
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for op in operations:
            
            if op[0] == '-':
                if op[1:].isdigit():
                    record.append(op)
                    
            elif op[0] != '-' and op.isdigit():
                record.append(op)

            elif op == '+':
                if len(record) >= 2:
                    score1, score2 = record[-2:]
                    record.append(int(score1) + int(score2))
            
            elif op == 'D':
                if len(record) >= 1:
                    record.append(2 * int(record[-1]))
            

            elif op == 'C':
                if len(record) >= 1:
                    record.pop()
        

            print(record)
            
        print(record)

        return sum([int(num) for num in record])

        