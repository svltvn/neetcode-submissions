class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        for c in s:
            if not t:
                return 0
            if c == t[0]:
                t=t[1:]
        
        return len(t)