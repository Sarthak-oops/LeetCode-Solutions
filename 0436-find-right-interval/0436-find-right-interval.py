class Solution:
    
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        def binarysearch(key):
            start=0
            end=n-1
            while(start<=end):
                mid=(start+end)//2
                if key==intervals[mid][0]:
                    return mid
                elif key<intervals[mid][0]:
                    end=mid-1
                else:
                    start=mid+1
            return start
        d={}
        n=len(intervals)
        res=[-1]*n
        
        for i in range(n):
            d[str(intervals[i])]=i
        intervals.sort()
        for i in range(n):
            index=binarysearch(intervals[i][1])
            if index<n:
                res[d[str(intervals[i])]]=d[str(intervals[index])]
        return res
    
            