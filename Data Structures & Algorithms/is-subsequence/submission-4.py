class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        for c in t:
            if not s:
                return True
            if c == s[0]:
                s = s[1:]
        
        return len(s) == 0