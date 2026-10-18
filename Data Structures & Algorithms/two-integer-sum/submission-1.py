class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for index in range(len(nums)):
            if target-nums[index] in values:
                return [values[target-nums[index]],index]
            else:
                values[nums[index]] = index