class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        
        returnArray = []
        while k > 0:
            returnArray.append(max(hashmap, key=hashmap.get))
            hashmap.pop(max(hashmap, key=hashmap.get))
            k-=1
        return returnArray