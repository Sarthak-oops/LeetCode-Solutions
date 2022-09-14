class Solution:
    def simplifyPath(self, path: str) -> str:
        x=path.split('/')
        l=[]
        for i in x:
            if i==".":
                continue
            elif i=="":
                continue
            elif i=="..":
                if(len(l)!=0):
                    l.pop()
            else:
                l.append(i)
        return "/"+"/".join(l)
            