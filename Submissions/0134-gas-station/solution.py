class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total = 0
        result = 0
        for i in range(len(gas)):
            total = total + (gas[i]-cost[i])
            if total < 0:
                result = i + 1
                total = 0
        return result
