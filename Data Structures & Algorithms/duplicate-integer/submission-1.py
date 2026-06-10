class Solution:
    '''
    BF first, then optimal
    '''
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsSet = set(nums)
        return len(numsSet) != len(nums)