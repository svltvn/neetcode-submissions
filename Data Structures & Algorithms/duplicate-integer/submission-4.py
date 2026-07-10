class Solution:
    '''
    BF first, then optimal
    '''
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Using length
        '''
        numsSet = set(nums)
        return len(numsSet) != len(nums)
        '''

        #Brute Force
        '''
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] == nums[j]:
                    return True
        return False
        '''

        #Optimal
        '''
        hashset = set()
        for i in range(len(nums)):
            if nums[i] in hashset:
                return True
            hashset.add(nums[i])
        return False
        '''

        #2nd try
        return len(set(nums)) != len(nums)