class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        hashmap = {'{':'}','(':')','[':']'}
        for c in s:
            #opening bracket
            if c in ['{','(','[']:
                stack.append(c)
                print(stack)
            #closing bracket
            else:
                if len(stack)==0 or hashmap[stack.pop()] != c:
                    return False
        return len(stack) == 0
