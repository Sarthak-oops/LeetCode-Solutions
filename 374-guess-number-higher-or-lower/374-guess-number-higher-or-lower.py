# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l=1
        r=n
        
        while True:
            mid=l+(r-l)//2
            x=guess(mid)
            if x==0:
                
                return mid
            elif x==1:
                l=mid+1
                r=n
            else:
                #l=mid
                r=mid-1
        