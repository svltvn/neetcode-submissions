class Solution:
    def isPalindrome(self, s: str) -> bool:       
        sArr = [c.lower() for c in s if c.isalnum()]
        print(sArr)
        print(sArr[::-1])

        return sArr == sArr[::-1]

