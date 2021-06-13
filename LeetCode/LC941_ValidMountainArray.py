
#941. Valid Mountain Array
'''
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
        arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
        arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

'''

#s1
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        i = 0
        j = len(arr)-1
        while(i<len(arr)-1):
            if arr[i+1] > arr[i]:
                i = i+1
            else:
                break
        while(j>1):
            if arr[j-1] > arr[j]:
                j = j-1
            else:
                break
        return (i == j and i!=0 and i!=len(arr)-1)
            
            
#s2           
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        m = arr.index(max(arr))
        if (m==0 or m == len(arr)-1):
            return False
        for i in range(len(arr)):
            if arr[i] >= arr[m] and i!=m:
                return False
            try:
                if (i<m and arr[i+1] <= arr[i]) or (i>m and arr[i+1] >= arr[i]):
                    return False
            except:
                pass
        return True
    
#s3
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        peak = False
        for i in range(len(arr)-1):
            if peak==False and arr[i]<arr[i+1]:
                pass
            elif i!= 0 and arr[i]>arr[i-1] and arr[i]>arr[i+1] and peak ==False:
                peak = True
            elif peak==True and arr[i]>arr[i+1]:
                pass
            else:
                return False
        return peak
            
            
            
            
