class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # Array to track max earnings possible at any point 0..i
        maxEarnings = [0] * len(nums)

        maxEarnings[0] = nums[0]
        maxEarnings[1] = max(maxEarnings[0], nums[1])

        for i in range(2, len(nums)):
            # Takes max between max at previous i vs at (i - 2) + current value
            maxEarnings[i] = max(maxEarnings[i - 1], maxEarnings[i-2] + nums[i])
        
        return maxEarnings[-1]


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