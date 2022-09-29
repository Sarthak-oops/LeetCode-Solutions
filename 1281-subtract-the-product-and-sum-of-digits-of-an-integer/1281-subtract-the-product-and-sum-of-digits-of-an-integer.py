class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod=1
        s=0
        while n!=0:
            x=n%10
            prod=prod*x
            s=s+x
            n=n//10
        return (prod-s)