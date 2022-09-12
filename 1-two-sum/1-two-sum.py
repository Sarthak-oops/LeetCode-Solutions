class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i in range(len(nums)):
            d1=nums[i]
            d2=target-d1
            if d2 in hashmap:
                return[i,hashmap[d2]]
            else:
                hashmap[d1]=i