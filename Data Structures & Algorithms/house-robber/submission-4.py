class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # Array to track max earnings at any point 0..i
        maxEarningsPossibleAt = [0] * len(nums)

        maxEarningsPossibleAt[0] = nums[0]
        maxEarningsPossibleAt[1] = max(maxEarningsPossibleAt[0], nums[1])

        for i in range(2, len(nums)):
            # Takes max between max at previous i vs at (i - 2) + current value
            maxEarningsPossibleAt[i] = max(maxEarningsPossibleAt[i - 1], maxEarningsPossibleAt[i-2] + nums[i])
        
        return maxEarningsPossibleAt[-1]


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