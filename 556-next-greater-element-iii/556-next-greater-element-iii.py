class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s=list(str(n))
        i=len(s)-2
        ss=""
        while i>=0 and s[i]>=s[i+1]:
            i-=1
        if i>=0:
            j=len(s)-1
            while(s[i]>=s[j]):
                j-=1
            s[j],s[i]=s[i],s[j]
            
            s=s[:i+1]+s[i+1:][::-1]
            ss=ss.join(s)
            if int(ss) <=2**31-1:
                return int(ss)
            else:
                return -1
        else:
            return -1