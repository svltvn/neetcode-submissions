class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))

        seqLen = maxLen =  0
        print(nums)
        for i in range(len(nums)):
            if (i==0) or (nums[i-1] == nums[i]-1):
                seqLen += 1
                maxLen = max(maxLen, seqLen)
            else:
                seqLen = 1
        
        return maxLen
            





        
