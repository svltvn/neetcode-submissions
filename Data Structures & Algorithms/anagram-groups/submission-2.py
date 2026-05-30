class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Second attempt, let's see if I can try to solve this by looking at the constraints, BF and then optimal sol
        '''
        hashmap = {}
        
        for s in strs:
            sortS = "".join(sorted(s))
            if sortS in hashmap:
                hashmap[sortS].append(s)
            else:
                hashmap[sortS] = [s]
        
        return list(hashmap.values())