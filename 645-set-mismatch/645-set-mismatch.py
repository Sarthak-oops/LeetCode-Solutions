class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in range(1,len(nums)+1):
            if i not in d:
                ans=i
            elif d[i]>1:
                ans1=i
        return ([ans1,ans])
            