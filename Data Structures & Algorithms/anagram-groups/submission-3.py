class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for s in strs:
            sSorted = "".join(sorted(s))
            if sSorted in hashmap:
                hashmap[sSorted].append(s)
            else:
                hashmap[sSorted] = [s]
        print(hashmap.values())
        return list(hashmap.values())