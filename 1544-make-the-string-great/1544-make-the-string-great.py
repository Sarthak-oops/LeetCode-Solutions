class Solution:
    def makeGood(self, s: str) -> str:
        if s=="":
            return ""
        if len(s)==1:
            return s
        stack=[s[0]]
        for i in range(1,len(s)):
            if(len(stack)==0):stack.append(s[i])
            else:
                if s[i].lower()==stack[-1].lower():
                    if s[i].islower() and stack[-1].isupper():
                        stack.pop()
                    elif s[i].isupper() and stack[-1].islower():
                        stack.pop()
                    else:
                        stack.append(s[i])
                else:
                    stack.append(s[i])
        return ''.join(stack)