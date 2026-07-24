class Solution:
    def isPalindrome(self, s: str) -> bool:       
        sArr = [c.lower() for c in s if c.isalnum()]
        
        return sArr == sArr[::-1]

