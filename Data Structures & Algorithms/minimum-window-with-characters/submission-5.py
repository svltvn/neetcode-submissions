class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tSplit = [c for c in t]
        res = []
        l = 0

        for r in range(len(s)):
            if s[r] in tSplit:
                tSplit.remove(s[r])
            
            while not tSplit:
                res.append(s[l:r+1])
                if s[l] in t:
                    # Count occurrences in current window vs requirements
                    window_part = s[l+1:r+1]
                    needed_in_t = t.count(s[l])
                    if window_part.count(s[l]) < needed_in_t:
                        tSplit.append(s[l])
                l += 1
            
        if not res:
            return ""
        else:
            return min(res, key=len)