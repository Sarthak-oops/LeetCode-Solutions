class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1,n):
            s=str(i)
            s1=str(n-i)
            if s.count("0")==0 and s1.count("0")==0:
                return [int(i),int(n-i)]
            