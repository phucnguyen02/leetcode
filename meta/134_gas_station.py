class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1

        total = res = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            if total < 0:
                total = 0
                res = i + 1

        return res
    
# The only case where there isn't a solution is where sum(gas) < sum(cost), because you won't have enough to traverse the entire circle
# When gas < cost, we can't go to the next station so we don't want to start at the current. Every time that happens, consider the next station as a potential
# starting point. If we reach the end of the list, the result is the starting station we last updated