class Solution:
    def rob(self, nums: List[int]) -> int:
        # Base Cases
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        elif len(nums) == 3:
            return max(nums[0], nums[1], nums[2])

        dp1 = [0] * (len(nums))
        dp2 = [0] * (len(nums))

        # Initialize dp1 and dp2 arrays
        dp1[0], dp2[1] = nums[0], nums[1]
        dp1[1], dp2[2] = max(dp1[0], nums[1]), max(dp2[1], nums[2])

        # Perform house robber I iteration on all except last house 
        for i in range(2, len(nums) - 1):
            dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i])

        # Perform house robber I iteration on all except first house 
        for j in range(3, len(nums)):
            print(j)
            dp2[j] = max(dp2[j - 1], dp2[j - 2] + nums[j])

        # Return which exclusion resulted in greater max earnings 
        return max(dp1[-2], dp2[-1])