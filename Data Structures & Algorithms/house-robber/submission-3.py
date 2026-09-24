class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)

        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i-2] + nums[i])
        
        return dp[-1]


        # Greedy Approach: Does not satisfy all cases
        # if len(nums) == 1:
        #     return nums[0]

        # maxMoney = 0
        
        # l, r = len(nums) - 2, len(nums) - 1

        # while l >= 0:
        #     if nums[l] > (nums[r] + nums[l - 1]):
        #         maxMoney += nums[l]
        #         print(nums[l])
        #         r -= 3
        #     else:
        #         maxMoney += nums[r]
        #         print(nums[r])
        #         r -= 2
        #     l = r - 1

        # if r >= 0:
        #     maxMoney += nums[r]
        
        # return maxMoney