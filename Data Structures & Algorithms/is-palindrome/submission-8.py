class Solution:
    def isPalindrome(self, s: str) -> bool:       
        sArr = []
        for c in s:
            if c.isalnum():
                sArr.append(c.lower())
        
        l, r = 0, len(sArr)-1
        while l<r:
            if sArr[l] == sArr[r]:
                l+=1
                r-=1
            else:
                return False
    
        return True

