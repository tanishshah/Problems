#242. Valid Anagram
'''
Given two strings s and t,
return true if t is an anagram of s, and false otherwise.
'''

#Solution 1 sorting
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

#alt
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        for char in s:
            try:
                letters[char] = letters[char]+1
            except:
                letters[char] = 1
        for char in t:
            try:
                letters[char] = letters[char]-1
            except:
                return False
        for element in letters:
            if letters[element] != 0:
                return False
        return True
