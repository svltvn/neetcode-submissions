class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        pair = []

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                pair = [hashmap[complement], i]
            else:
                hashmap[nums[i]] = i
        
        return pair