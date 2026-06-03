class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            row = [1] * (i+1)
            for j in range(1, len(row)-1, 1):
                prevRow = res[-1]
                row[j] = prevRow[j-1]+prevRow[j]
            res.append(row)

        return res 