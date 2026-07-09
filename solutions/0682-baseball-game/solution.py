class Solution:
    def calPoints(self, operations: list[str]) -> int:
        res = []
        for i in range(len(operations)):
            if operations[i].lstrip('-').isdigit():
                res.append(int(operations[i]))
            elif operations[i] == '+':
                res.append(res[-1] + res[-2])
            elif operations[i] == 'D':
                res.append(res[-1] * 2)
            elif operations[i] == 'C':
                res.pop()
                
        return sum(res)

