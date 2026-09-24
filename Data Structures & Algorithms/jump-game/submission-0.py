class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # furthestIndex = [0] * len(nums)

        # for i in range(len(nums)):
        #     furthestIndex[i] = i + nums[i]
        #     if furthestIndex[i] >= len(nums) - 1:
        #         return True

        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if (i + nums[i]) >= goal:
                goal = i

        return goal == 0

        
