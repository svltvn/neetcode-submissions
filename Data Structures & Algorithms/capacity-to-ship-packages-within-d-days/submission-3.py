class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        '''
        Thinking about capacity of a ship:
            - What would be the lowest bound capacity and the highest bound capacity?
                Lowest capacity, will be the max(weights)
                Highest capacity, will be the sum(weights) = 1 day
        '''
        l, r = max(weights), sum(weights)
        res = r

        def canShip(cap):
            ships, currCap = 1, cap
            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    currCap = cap

                currCap -= w
            return True

        while l <= r:
            cap = (l + r) // 2
            if canShip(cap):
                res = min(res, cap)
                r = cap - 1
            else:
                l = cap + 1

        return res