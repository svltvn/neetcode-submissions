class Solution:
    def isPalindrome(self, s: str) -> bool:
        s="".join(c.lower() for c in s if c.isalnum() )

        for i in range(len(s)//2):
            j= (i+1) * -1
            if s[i] != s[j]:
                return False
        return True