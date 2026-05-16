class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            # target < l or target > r?
            if target <= nums[l]:
                return l
            elif nums[r] < target:
                return r+1
            elif nums[r] == target:
                return r


            m = (r-l) // 2 + l
            if target < nums[m+1]:
                r = m
            else:
                l = m+1