class Solution:
    def reverseVowels(self, s: str) -> str:
        v=['a','e','i','o','u','A','E','I','O','U']
        i=0
        j=len(s)-1
        l=list(s)
        while i<j:
            if l[i] in v and l[j] in v:
                l[i],l[j]=l[j],l[i]
                i+=1
                j-=1
            elif l[i] not in v:
                i+=1
            elif l[j] not in v:
                j-=1
        return ''.join(l)