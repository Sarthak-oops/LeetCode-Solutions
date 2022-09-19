class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d={0:1}
        c=0
        for i in range(1,len(nums)):
            nums[i]=nums[i]+nums[i-1]
        for i in nums:
            if i-k in d:
                c+=d[i-k]
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        return c
                