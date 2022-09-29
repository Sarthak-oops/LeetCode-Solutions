class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        s=set(s1)
        ss=set(s2)
        c=0
        if s!=ss:
            return False
        if s1==s2:
            return True
        if len(s1)!=len(s2):
            return False
        for i in s1:
            if s1.count(i)!=s2.count(i):
                return False
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                c+=1
        if c==2:
            return True
        else:
            return False