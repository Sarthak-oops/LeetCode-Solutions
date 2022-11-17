class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d={}
        for i in chars:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        
        res=0
        for i in words:
            flag=0
            d1=d.copy()
            #print(d1)
            for j in i:
                if j in d1 and d1[j]!=0:
                    d1[j]-=1
                else:
                    flag=1
                    
            if flag==0:
                res=res+len(i)
            flag=0
        
        return res