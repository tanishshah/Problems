#645. Set Mismatch
'''
You have a set of integers s, which originally contains all
the numbers from 1 to n. Unfortunately, due to some error,
one of the numbers in s got duplicated to another number in the set,
which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of
this set after the error.

Find the number that occurs twice and the number that is missing and
return them in the form of an array.
'''
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s1 = sum(nums)
        total = 0
        for i in range(1,len(nums)+1):
            total+=i
        nums = set(nums)
        s2 = sum(nums)
        res = []
        res.append(s1-s2)
        res.append(total-s2)
        return res
