class Solution:
    def calPoints(self, operations: List[str]) -> int:
        l=[]
        for i in range(len(operations)):
            if operations[i]=='+':
                l.append(l[-1]+l[-2])
            elif operations[i]=='C':
                l.pop()
            elif operations[i]=='D':
                l.append(l[-1]*2)
            else:
                l.append(int(operations[i]))
        return sum(l)