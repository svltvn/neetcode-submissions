class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        Second attempt here, will break down constraints, BF and then BS
        '''

        for i in range(len(nums)):
            if nums[i] == target:
                return i

        return -1