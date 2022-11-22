class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        final=[]
        for i in nums1:
            if i in nums2 or i in nums3:
                final.append(i)
        for j in nums2:
            if j in nums3:
                final.append(j)
                
        return (set(final))