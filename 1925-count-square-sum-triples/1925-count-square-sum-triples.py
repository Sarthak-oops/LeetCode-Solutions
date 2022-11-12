class Solution:
    def countTriples(self, n: int) -> int:
        square=[]
        c=0
        for i in range(1,n+1):
            square.append(i**2)
        for i in range(3,n-1):
            for j in range(i+1,n):
                if ((i**2)+(j**2)) in square:
                    c+=2
        return c