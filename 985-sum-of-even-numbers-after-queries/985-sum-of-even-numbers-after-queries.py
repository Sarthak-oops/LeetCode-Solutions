class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res=[]
        s=0
        for i in nums:
            if(i%2==0):
                s+=i
        for i in range(len(queries)):
            x=queries[i][1]
            if nums[x]%2==0:
                s=s-nums[x]
            nums[x]=nums[x]+queries[i][0]
            if nums[x]%2==0:
                s=s+nums[x]
            res.append(s)
        return res