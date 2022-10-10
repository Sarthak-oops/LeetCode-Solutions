class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        gcd=numsDivide[0]
        c=0
        for i in numsDivide:
            gcd=math.gcd(gcd,i)
        nums.sort()
        for i in nums:
            if gcd%i==0:
                return c
            else:
                c+=1
        return -1