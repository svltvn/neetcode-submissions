class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = ['{', '(', '[']
        parDict = {'{':'}', '(':')', '[':']'}

        for c in s:
            if c in open:
                stack.append(c)
            elif stack:
                openP = stack.pop()
                if parDict[openP] != c:
                    return False
            else:
                return False
        
        return not stack

