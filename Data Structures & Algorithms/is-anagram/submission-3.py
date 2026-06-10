class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Brute Force
        if len(s) != len(t):
            return False
        sHashmap, tHashmap = {}, {}

        for i in range(len(s)):
            sHashmap[s[i]] = sHashmap.get(s[i], 0) + 1
            tHashmap[t[i]] = tHashmap.get(t[i], 0) + 1
        print(sHashmap, tHashmap)
        return sHashmap == tHashmap