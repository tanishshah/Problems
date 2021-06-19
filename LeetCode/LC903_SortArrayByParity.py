#905. Sort Array By Parity
'''
Given an array nums of non-negative integers,
return an array consisting of all the even elements of nums,
followed by all the odd elements of nums.

You may return any answer array that satisfies this condition.
'''
#sol1
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        pos = len(nums)-1
        i = 0
        while i<pos:
            if nums[i]%2!=0:
                temp = nums[i]
                nums[i] = nums[pos]
                nums[pos] = temp
                if nums[i]%2!= 0:
                    pos-=1
            else:
                i+=1
        return nums


#slower
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        pos = len(nums)
        i = 0
        while i<pos:
            if nums[i]%2!=0:
                nums.insert(pos,nums[i])
                nums.pop(i)
                pos-=1
            else:
                i+=1
        return nums
