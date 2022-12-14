class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        prev2 = nums[0]
        moneyRobbed = prev1 = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            moneyRobbed = max(prev1, prev2+nums[i])

            prev2 = prev1
            prev1 = moneyRobbed

        return moneyRobbed