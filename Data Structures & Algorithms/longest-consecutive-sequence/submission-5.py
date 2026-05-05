class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(sorted(set(nums)))
        print(nums)
        l = 0
        r = 1
        maxSeq = 0
        if len(nums) == 0:
            return 0
        while r < len(nums):
            if nums[l]+(maxSeq+1) == nums[r]:
                print(nums[l], nums[r],maxSeq)
                maxSeq = max(maxSeq, r-l)
                r += 1
            else:
                l, r = r, l+1
        return maxSeq+1





        
