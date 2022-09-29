class Solution:
    def hammingWeight(self, n: int) -> int:
        n=int(str(n))
        n=bin(n).replace('0b','')
        c=n.count('1')
        return c