class Solution:
    def countLargestGroup(self, n: int) -> int:
        d={}
        s=0
        for i in range(1,n+1):
            x=i
            while x!=0:
                s=s+x%10
                x=x//10
            if s not in d:
                d[s]=[i]
            else:
                d[s].append(i)
            s=0
        m=-99999
        for i in d:
            if len(d[i])>m:
                m=len(d[i])
                count=1
            elif len(d[i])==m:
                count+=1
        return count
            