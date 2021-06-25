#Leetcode 125 Valid Palindrone
'''
Given a string s, determine if it is a palindrome
considering only alphanumeric characters and ignoring cases.
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        clean = ""
        for char in s:
            if char.isalnum():
                clean = clean+char
        i = 0
        j = len(clean)-1
        for i in range(len(clean)):
            if clean[i]!=clean[j]:
                return False
            if i >= j:
                break
            i = i+1
            j = j-1
        return True
