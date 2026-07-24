class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        sArr = [c.lower() for c in s if c.isalnum()]


        l, r = 0, len(sArr)-1
        while l<r:
            if sArr[l] != sArr[r]:
                return False
            l += 1
            r -= 1
        
        return True

