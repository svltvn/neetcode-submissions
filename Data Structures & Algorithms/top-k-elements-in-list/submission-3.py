class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        returnArray = []
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        while k > 0:
            returnArray.append(max(hashmap, key=hashmap.get))
            hashmap.pop(max(hashmap, key=hashmap.get))
            k -= 1
        
        return returnArray
        