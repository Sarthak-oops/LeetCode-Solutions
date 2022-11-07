class Solution:
    def maximum69Number (self, num: int) -> int:
        s=list(str(num))
        flag=0
        for i in range(len(s)):
            if s[i]!='9':
                s[i]='9'
                flag=1
            if flag==1:
                return ''.join(s)
        return ''.join(s)