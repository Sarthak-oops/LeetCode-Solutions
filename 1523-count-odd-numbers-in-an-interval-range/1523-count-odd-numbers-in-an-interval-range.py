class Solution:
    def countOdds(self, low: int, high: int) -> int:
        c=0
        if low%2!=0:
            c+=1
        elif high%2!=0:
            c+=1
        c=c+(high-low)//2
        return c