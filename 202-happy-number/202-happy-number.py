class Solution:
    def isHappy(self, n: int) -> bool:
        d={}
        d[n]=1
        s=0
        while True:
            if n!=0:
                x=n%10
                s=s+x**2
                n=n//10
            else:
                if s==1:
                    return True
                else:
                    if s in d:
                        return False
                    else:
                        d[s]=1
                    n=s
                    s=0