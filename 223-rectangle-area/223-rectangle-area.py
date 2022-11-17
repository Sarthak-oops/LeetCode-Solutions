class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        d=[]
        x=[]
        d1=[]
        x1=[]
        l1=abs(ax1-ax2)
        b1=abs(ay1-ay2)
        l2=abs(bx1-bx2)
        b2=abs(by1-by2)
        #print(l1,b1,l2,b2)
        for i in range(ax1,ax2+1):
            d.append(i)
        
        for i in range(bx1,bx2+1):
            if i in d:
                x.append(i)
        
        for i in range(ay1,ay2+1):
            d1.append(i)
        
        for i in range(by1,by2+1):
            if i in d1:
                x1.append(i)
        
        cl=len(x)
        cb=len(x1)
        area=l1*b1+l2*b2
        if cl==0 or cb==0:
            return area
        else:
            area=area-((cl-1)*(cb-1))
            return area