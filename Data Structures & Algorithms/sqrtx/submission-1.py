class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = 0
        while l<=r:
            m = (r-l)//2+l
            mS = m*m
            if x < mS:
                r = m -1
            elif mS < x:
                l = m+1
                res = m
            else:
                return m

        
        return res
