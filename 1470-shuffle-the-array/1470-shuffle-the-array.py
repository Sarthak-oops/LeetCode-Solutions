class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x=nums[0:n]
        y=nums[n:]
        nums=[]
        for i in range(n):
            nums.append(x[i])
            nums.append(y[i])
        return nums