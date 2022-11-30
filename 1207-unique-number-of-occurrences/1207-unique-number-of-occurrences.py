class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        d1={}
        l=[]
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in d:
            l.append(d[i])
        for i in l:
            if i not in d1:
                d1[i]=1
            else:
                d1[i]+=1
        for i in d1:
            if d1[i]>1:
                return False
        return True