class Solution:
    def reverseWords(self, s: str) -> str:
        s1=""
        l=list(s[::-1].split())
        l=l[::-1]
        for i in range(len(l)-1):
            s1=s1+''.join(l[i])+" "
        return s1+''.join(l[-1])
        