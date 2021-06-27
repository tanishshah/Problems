
#350. Intersection of Two Arrays II
'''
Given two integer arrays nums1 and nums2,
return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
'''

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums = {}
        for x in range(len(nums1)):
            try:
                a = nums[nums1[x]]
                nums[nums1[x]] = nums[nums1[x]]+1
            except:
                nums[nums1[x]] = 1
                
        res = []     
        for x in range(len(nums2)):
            try: 
                if nums[nums2[x]] > 0:
                    nums[nums2[x]] = nums[nums2[x]]-1
                    res.append(nums2[x])
            except:
                pass
        return res

        
