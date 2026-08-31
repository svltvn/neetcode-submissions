class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #While loop, len(stones) > 1
        ##get max(2 of stones), pop each other, minus each other
        ##if 0, don't do anything
        ##if abs(diff) > 0, then add that back in
        while len(stones) > 1:
            stones = sorted(stones)
            print(stones)
            diff = abs(stones.pop()-stones.pop())
            if diff > 0:
                stones.append(diff)
        
        if stones:
            return stones[0]
        else: 
            return 0