class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[0]>=target:
            return 0
        elif nums[len(nums)-1] < target:
            return len(nums)
        elif nums[len(nums)-1]== target:
            return len(nums)-1
        
        for i in range(len(nums)-1):
            if nums[i] == target:
                return i
            elif nums[i] < target and nums[i+1] > target:
                return i+1