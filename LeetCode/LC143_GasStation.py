#143 Gas Station
'''
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station.
You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station'
index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique
'''

#Solution 1
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        check = []
        for i in range(len(gas)):
            if gas[i] >= cost[i]:
                check.append(i)
        for i in check:
            j = i
            count = 0
            left = 0
            while left >=0:
                left += gas[j%len(gas)]
                left -=cost[j%len(gas)]
                j += 1
                count += 1
                if count == len(gas) and left>=0:
                    return i
        return -1
