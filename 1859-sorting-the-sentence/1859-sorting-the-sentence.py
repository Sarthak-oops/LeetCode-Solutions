class Solution:
    def sortSentence(self, s: str) -> str:
        d={}
        c=""
        l=list(s.split())
        for i in l:
            d[i[-1]]=i[:len(i)-1]
        d=sorted(d.items())
        for i in d:
            c=c+i[1]+" "
        return c[:-1]
            