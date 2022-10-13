class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res=""
        
        
        a=[str(s1) for s1 in nums]
        for i in range(len(a)-1):
            for j in range(i+1,len(a)):
                if int(a[i]+a[j])<int(a[j]+a[i]):
                    a[i],a[j]=a[j],a[i]
        x="".join(a)
        return str(int(x))