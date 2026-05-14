class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1, p2 = 0, 0
        if not s:
            return True

        while p2 < len(t):
            print(s[p1], t[p2])
            if s[p1] == t[p2]:
                p1+=1
                if p1 == len(s):
                    return True
            p2 += 1
        
        return False