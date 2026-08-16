class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                num = nums[i]+nums[j]
                if num == target and i != j:
                    return [i,j]