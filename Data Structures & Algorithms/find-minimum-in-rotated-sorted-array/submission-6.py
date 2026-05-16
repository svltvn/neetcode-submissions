class Solution:
    def findMin(self, nums: List[int]) -> int:
        #2Pointer Approach
        # If both subarrs are sorted, pick min(l, m)
        # if one subarr not sorted, pick that one
        l, r = 0, len(nums)-1
        minNum = nums[0]
        while l < r:
            print(l,r, nums[l:r])
            m = ((r-l)//2)+ l
            if nums[l] < nums[m] and nums[m+1] < nums[r]:
                return min(nums[l], nums[m+1])
            elif nums[l] > nums[m]:
                r = m
                minNum = min(minNum, nums[l], nums[m])
            else:
                l=m+1
                minNum = min(minNum, nums[m+1],nums[r])
        return minNum