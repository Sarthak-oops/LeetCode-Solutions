class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l=[]
        s=""
        s1=""
        n=0
        if digits[-1]!=9:
            digits[-1]+=1
            return digits
        else:
            for i in digits:
                s+=str(i)
            n=int(s)
            n+=1
            s1=str(n)
            for i in s1:
                l.append(i)
            return l