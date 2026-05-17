class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        minOp = k
        for i in range(len(blocks)-(k-1)):
            begin = i
            end = i+k
            subS = blocks[begin:end]
            op = 0
            for c in subS:
                if c == "W":
                    op += 1
            
            minOp = min(minOp, op)
        
        return minOp