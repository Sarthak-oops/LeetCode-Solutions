class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        s=len(set(candyType))
        n=len(candyType)
        m=n//2
        if s<=m:
            return s
        else:
            return m