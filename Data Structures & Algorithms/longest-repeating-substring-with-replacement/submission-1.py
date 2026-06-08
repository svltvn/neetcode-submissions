class Solution:
    '''
    I've tried this problem many times, still can't get it going, for now going to copy over the code, but definitely a question to revisit 
    '''
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0

        for r in range(len(s)):
            #add this to freq hashmap 
            count[s[r]] = count.get(s[r], 0)+1

            #check validity of string
            if r-l+1 - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            #update max length
            res = max(res, r-l+1)
        return res