class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        returnArray = []
        for num in hashmap:
            if hashmap[num] > len(nums)//3:
                returnArray.append(num)
        
        return returnArray