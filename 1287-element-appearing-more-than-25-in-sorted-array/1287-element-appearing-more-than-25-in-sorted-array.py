class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        d={}
        m=len(arr)/4
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in d:
            if d[i]>m:
                return i