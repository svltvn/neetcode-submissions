class Solution:
    '''
    BF first, optimal seond
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #BF Solution
        '''
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i]+nums[j] == target:
                    return [i, j]
        '''

        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                return [hashmap[nums[i]], i]
            else:
                rem = target - nums[i]
                hashmap[rem] = i
