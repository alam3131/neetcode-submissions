class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if (i + nums[i]) >= goal:
                goal = i

        return goal == 0

        # What exactly makes this greedy?
        # 
        # At each index, you make a locally optimal choice:
        # If this index can reach my current known-good position, move the goal here.

        
