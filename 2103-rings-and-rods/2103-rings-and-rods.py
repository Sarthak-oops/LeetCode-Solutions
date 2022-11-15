class Solution:
    def countPoints(self, rings: str) -> int:
        d={}
        for i in range(1,len(rings),2):
            if rings[i] not in d:
                d[rings[i]]=[rings[i-1]]
            else:
                d[rings[i]].append(rings[i-1])
        
        c=0
        for i in d:
            if len(set(d[i]))==3:
                c+=1
        return c