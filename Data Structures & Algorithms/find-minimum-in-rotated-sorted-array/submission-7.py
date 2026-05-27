class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        Done this problem before, but let's try to attempt it again
        '''
        minNum = max(nums)
        for num in nums:
            minNum = min(minNum, num)

        return minNum

        