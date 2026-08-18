class Solution:
    def isPalindrome(self, s: str) -> bool:       
        sortedS = ""
        for c in s:
            if c.isalnum():
                sortedS += c.lower()
    

        return sortedS == sortedS[::-1]