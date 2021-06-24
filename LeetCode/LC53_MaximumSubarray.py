'''
LC 53 Maximum subarray
Given an integer array nums, find the contiguous subarray
containing at least one number)
which has the largest sum and return its sum.
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = -99999999
        max = -99999999
        i = 0
        for i in range(len(nums)):
            if i ==0:
                sum = nums[i]
            else:
                if nums[i] >= nums[i] + sum:
                    sum = nums[i]
                else:
                    sum = sum + nums[i]
            if sum>max:
                max = sum
        return max
                    
        
                
                
                
            
            
        
