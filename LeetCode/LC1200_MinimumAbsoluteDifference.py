#1200. Minimum Absolute Difference
'''
Given an array of distinct integers arr, find all pairs of elements
with the minimum absolute difference of any two elements. 

Return a list of pairs in ascending order(with respect to pairs),
each pair [a, b] follows

    a, b are from arr
    a < b
    b - a equals to the minimum absolute difference of
    any two elements in arr
'''

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        diff = 2*(10**6)+1
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] < diff:
                diff = arr[i+1] - arr[i]
        res = []
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] == diff:
                a =[]
                a.append(arr[i])
                a.append(arr[i+1])
                res.append(a)
        return res
