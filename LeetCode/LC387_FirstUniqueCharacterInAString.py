#387. First Unique Character in a String
'''
Given a string s, return the first non-repeating character in it
and return its index.If it does not exist, return -1.
'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters = {}
        for i in range(len(s)):
            try:
                letters[s[i]]+= 0
                letters[s[i]]=-1
            except:
                letters[s[i]] = i
        index = (10**5) + 1
        for k in letters:
            if letters[k] !=-1 and letters[k]<index:
                index = letters[k]
        if index == (10**5) + 1:
            return - 1
        return index
