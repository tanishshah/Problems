#43. Multiply Strings

'''
Given two non-negative integers num1 and num2 represented as strings,
return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the
inputs to integer directly.
'''

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        total = 0
        for i in range(len(num1)):
            n1 = int(num1[i])
            n1 *= 10**(len(num1)-1-i)
            for j in range(len(num2)):
                n2 = int(num2[j])
                n2 *= 10**(len(num2)-1-j)
                total+=n2*n1
        return str(total)
