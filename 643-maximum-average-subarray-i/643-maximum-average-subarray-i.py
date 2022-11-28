class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i=k
        j=0
        n=len(nums)
        s=m=sum(nums[:k])
        while i<n:
            s=s+nums[i]-nums[j]
            j+=1
            i+=1
            m=max(m,s)
        return m/k
        