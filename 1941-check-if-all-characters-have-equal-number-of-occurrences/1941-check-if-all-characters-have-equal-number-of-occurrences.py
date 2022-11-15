class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        l=[]
        for i in d:
            l.append(d[i])
        if len(set(l))==1:
            return True
        else:
            return False