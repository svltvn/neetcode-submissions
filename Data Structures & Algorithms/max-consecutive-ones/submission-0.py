class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxStr = 0
        currentCount = 0
        for num in nums:
            if num == 1:
                currentCount +=1
            else:
                currentCount = 0
            maxStr = max(maxStr, currentCount)
        
        return maxStr