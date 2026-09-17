class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for i in range(len(nums)):
            complementNum = target - nums[i]
            if complementNum in numMap:
                return [numMap[complementNum], i]
            else:
                numMap[nums[i]] = i

        return []

