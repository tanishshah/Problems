#super ineffecient solution

'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        if len(nums)<3:
            return []
        i = 0
        j = 1
        res = []
        k = len(nums)-1
        while(i<len(nums)):
            if nums[i] + nums[k] + nums[j] == 0 :
                a = []
                a.append(nums[i])
                a.append(nums[j])
                a.append(nums[k])
                if a not in res:
                    res.append(a)
                if j + 1 !=k:
                    j = j+1
                elif i+2 != len(nums)-1:
                    i = i+1
                    j = i+1
                    k = len(nums) - 1
                else:
                    return res
            elif nums[i] + nums[j] + nums[k] < 0:
                if j + 1 !=k:
                    j = j+1
                elif i+2 != len(nums)-1:
                    i = i+1
                    j = i+1
                    k = len(nums) - 1
                else:
                    return res
            else:
                if k - 1 != j:
                    k = k -1
                elif i+2 != len(nums)-1:
                    i = i+1
                    j = i+1
                    k = len(nums) - 1
                else:
                    return res
        return res
            
