class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        s=0
        m=0
        ps=[]
        d={}
        index=0
        for i in range(len(nums)):
            if nums[i]==0:
                nums[i]=-1
        for i in nums:
            s+=i
            ps.append(s)
        for i in range(len(ps)):
            if ps[i] not in d:
                d[ps[i]]=i
        for i in range(len(ps)):
            if ps[i] in d:
                m1=i-d[ps[i]]
                if m1>m:
                    m=m1
        for i in range(len(ps)-1,-1,-1):
            if ps[i]==0:
                index=i+1
                break
        return max(m,index)