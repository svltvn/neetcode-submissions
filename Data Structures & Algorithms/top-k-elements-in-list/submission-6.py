class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}
        for num in nums:
            countMap[num] = countMap.get(num, 0) + 1
        print(countMap)
        res = []
        for i in range(k): 
            maxkey = max(countMap, key= lambda k: countMap[k]) #get an error, so have to do a lambda function
            countMap.pop(maxkey)
            res.append(maxkey)
        
        return res
