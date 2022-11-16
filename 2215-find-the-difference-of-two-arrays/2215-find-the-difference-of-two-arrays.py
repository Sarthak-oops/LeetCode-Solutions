class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        l1=[]
        l2=[]
        for i in nums1:
            if i not in nums2:
                l1.append(i)
        l1=list(set(l1))
        for i in nums2:
            if i not in nums1:
                l2.append(i)
        l2=list(set(l2))
        return [l1,l2]