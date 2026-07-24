class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            tank = 0
            for j in range(len(gas)):
                tank += gas[j]
                tank -= cost[j]
                if tank < 0:
                    gas.append(gas.pop(0))
                    cost.append(cost.pop(0))
                    break
                if j == len(gas)-1:
                    return i
        return -1