class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min=abs(arr[1]-arr[0])
        l=[]
        l.append([arr[0],arr[1]])
        for i in range(1,len(arr)-1):
            if abs(arr[i+1]-arr[i])==min:
                l.append([arr[i],arr[i+1]])
            elif abs(arr[i+1]-arr[i])<min:
                l=[]
                l.append([arr[i],arr[i+1]])
                min=abs(arr[i+1]-arr[i])
        return l
                