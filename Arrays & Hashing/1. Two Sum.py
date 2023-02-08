class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for index, num in enumerate(nums):
            if (target - num) in seen:
                return [seen[target-num], index]
            else:
                seen[num] = index
