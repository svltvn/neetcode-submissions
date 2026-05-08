class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        substring = ""
        minString = min(strs)
    
        for i in range(len(minString)):
            for s in strs:
                if minString[i] != s[i]:
                    return substring
            substring += minString[i]
                
                


        return substring
        