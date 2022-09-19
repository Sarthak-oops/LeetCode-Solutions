import math
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        rem=[]
        d={}
        c=0
        for i in range(1,len(nums)):
            nums[i]=nums[i]+nums[i-1]
        rem=[i%k for i in nums]
        
        rem.insert(0,0)
        for i in rem:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in d:
            if d[i]>1:
                c+=(d[i]*(d[i]-1))//2
        return c