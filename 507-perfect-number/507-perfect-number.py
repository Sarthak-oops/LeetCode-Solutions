class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        res=1
        if num==1:
            return False
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                res=res+i
                if num//i!=i:
                    res=res+num//i
        if res==num:
            return True
        return False