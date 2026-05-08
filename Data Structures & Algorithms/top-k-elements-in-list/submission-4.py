class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        

        returnList = []
        for i in range(k):
            maxNum = max(hashmap, key=hashmap.get)
            hashmap.pop(maxNum)
            returnList.append(maxNum)
        return returnList
            