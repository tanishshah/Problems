#504. Base 7
'''
Given an integer num, return a string of its base 7 representation.
'''
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        neg = ""
        if num<0:
            neg="-"
        
        num = abs(num)
        e = floor(log(num,7))
        vals = [0] * (e+1)  
        
        while(e>-1):
            k = num/(7**e)
            print(k)
            if k>=1:
                vals[len(vals)-1-e]=floor(k)
            num -= (7**e)*floor(k)
            e-=1
            if num == 0:
                break
        s = ""
        s += neg
        
        for val in vals:
            s += str(val)
        return s
