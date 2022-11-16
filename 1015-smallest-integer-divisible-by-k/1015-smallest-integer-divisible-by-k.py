class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k%2==0 or k%5==0:
            return -1
        n=1
        while True:
            if n%k==0:
                return len(str(n))
            else:
                n=n*10+1
        return -1