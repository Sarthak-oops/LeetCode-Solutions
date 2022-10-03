class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
            
        rem=[]
        d={0:-1}
        c=0
        for i in range(1,len(nums)):
            nums[i]=nums[i]+nums[i-1]
        rem=[i%k for i in nums]
        for i in range(len(rem)):
            if rem[i] not in d:
                d[rem[i]]=i
            #else:
             #   d[i]+=1
        for i in range(len(rem)):
            if i-d[rem[i]]>1:
                return True
        return False