#Leet Code 228 Summary Ranges
'''
You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all
the numbers in the array exactly. That is, each element of nums
is covered by exactly one of the ranges, and there is no integer x
such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

    "a->b" if a != b
    "a" if a == b

'''
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        initial = None
        prev = None
        for i in nums:
            if nums.index(i) == 0:
                initial = i
                prev = i
            elif i == prev + 1:
                prev = i
            else:
                if initial == prev:
                    res.append(str(initial))
                else:
                    res.append(str(initial) + "->"+ str(prev))
                prev = i
                initial = i
        if initial!=None:
            if initial == prev:
                res.append(str(initial))
            else:
                res.append(str(initial) + "->"+ str(prev))        
        return res
        
