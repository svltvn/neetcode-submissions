class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l<=r:
            m = (r-l)//2 + l
            hours = [math.ceil(pile/m) for pile in piles]

            if sum(hours) <= h:
                r = m-1
                res = min(res, m)
            else:
                l = m+1
        
        return res
        

        