class Solution:
    def findMin(self, nums: List[int]) -> int:
        minVal = 1001
        for i in range(len(nums)):
            minVal = min(minVal, nums[i])
        
        return minVal


        