class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left,right+1):
            x= i
            res= True
            if "0" not in str(i):
                while x != 0:
                    y = x % 10
                    if i%y!=0:
                        res = False
                    x= x // 10
                if res: ans.append(i)
        return ans