class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []

        for o in operations:
            if o == 'D':
                scores.append(scores[-1]*2)
            elif o == 'C':
                scores.pop()
            elif o == '+':
                scores.append(scores[-1]+scores[-2])
            else:
                num = int(o)
                scores.append(num)

        return sum(scores)