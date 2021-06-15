#LeetCode 205 Isomorphic Strings
'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.
'''

#solution 
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        cipher = {}
        for i in range(len(s)):
            try:
                k = cipher[s[i]]
            except KeyError:
                if t[i] not in cipher.values():
                    cipher[s[i]] = t[i]
        print(cipher)
        k =""
        for j in range(len(s)):
            try:
                k = k + cipher[s[j]]
            except KeyError:
                return False
        
        print(k)
        return(k == t)

#alt solution attempt
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        cipher1 = {}
        cipher2 = {}
        k = ""
        l = ""
        count1 = 0
        count2 = 0
        for i in range(len(s)):
            try:
                q = cipher1[s[i]]
            except KeyError:
                cipher1[s[i]] = count1
                count1 = count1 + 1
            try:
                q = cipher2[t[i]]
            except KeyError:
                cipher2[t[i]] = count2
                count2 = count2 + 1
        for i in range(len(s)):
            k = k + str(cipher1[s[i]])
            l = l + str(cipher2[t[i]])
        return (k == l)
        
