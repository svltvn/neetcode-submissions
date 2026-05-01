class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for str in strs:
            sortStr = "".join(sorted(str))
            if sortStr not in hashmap:
                hashmap[sortStr] = [str]
            else:
                hashmap[sortStr].append(str)
        
        return list(hashmap.values())