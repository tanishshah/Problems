#137 Single Number II

'''
Given an integer array nums where every element appears three times
except for one,which appears exactly once. Find the single element
and return it.

You must implement a solution with a linear runtime complexity
and use only constant extra space.
'''
#sol 1
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s1 = 0
        s2 = 0
        for i in nums:
            s1 += i
        nums = set(nums)
        for i in nums:
            s2+=i
        return int((3*s2 -s1)/2)
