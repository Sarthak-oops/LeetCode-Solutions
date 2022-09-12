class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        d=[]
        l=[0]*60
        c=0
        for i in range(len(time)):
            x=time[i]%60
            l[x%60]+=1
        if l[0]>1:
            c+=(l[0]*(l[0]-1))//2
        if l[30]>1:
            c+=(l[30]*(l[30]-1))//2
        i=1
        j=59
        while(i<j):
            c+=l[i]*l[j]
            i+=1
            j-=1
        return c