class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            '(':')',
            '{':'}',
            '[':']'
        }

        stack = []
        print(list(map.keys()))
        for c in s:
            if c in list(map.keys()):
                stack.append(c)
            else:
                if not stack or c != map[stack.pop()]:
                    return False
        
        return len(stack) == 0