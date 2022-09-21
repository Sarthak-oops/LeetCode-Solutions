class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        travel.insert(0,0)
        g=0
        p=0
        m=0
        lp,lg,lm=0,0,0
        res=0
        for i in range(1,len(travel)):
            travel[i]+=travel[i-1]
        for i in garbage:
            g+=i.count('G')
            p+=i.count('P')
            m+=i.count('M')
        for i in range(len(garbage)-1,-1,-1):
            if 'G' in garbage[i]:
                lg=i
                print(lg)
                break
            else:
                lg=0
        for i in range(len(garbage)-1,-1,-1):
            if 'P' in garbage[i]:
                lp=i
                print(lp)
                break
            else:
                lp=0
        for i in range(len(garbage)-1,-1,-1):
            if 'M' in garbage[i]:
                lm=i
                print(lm)
                break
            else:
                lm=0
        res=travel[lg]+g+travel[lp]+p+travel[lm]+m
        return res
            