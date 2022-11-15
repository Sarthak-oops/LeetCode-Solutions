class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d={}
        nums.sort()
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        m=-99999
        a=-1
        for i in d:
            if i%2==0:
                if d[i]>m:
                    m=d[i]
                    a=i
        return a