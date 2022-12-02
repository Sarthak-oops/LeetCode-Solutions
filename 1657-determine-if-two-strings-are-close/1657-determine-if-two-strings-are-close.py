class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        d2={}
        d1={}
        l1=[]
        l2=[]
        c1=[]
        c2=[]
        for i in word1:
            if i not in d1:
                d1[i]=1
                l1.append(i)
            else:
                d1[i]+=1
        for i in word2:
            if i not in d2:
                d2[i]=1
                l2.append(i)
            else:
                d2[i]+=1
        for i in d1:
            c1.append(d1[i])
        for i in d2:
            c2.append(d2[i])
        l1.sort()
        l2.sort()
        c1.sort()
        c2.sort()
        if l1==l2 and c1==c2:
            return True
        else:
            return False