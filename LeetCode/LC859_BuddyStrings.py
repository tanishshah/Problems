#859. Buddy Strings

'''
Given two strings s and goal, return true if you can swap two letters in s
so the result is equal to goal, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed)
such that i != j and swapping the characters at s[i] and s[j].

    For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
'''

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        good = False
        swap = False
        for i in range(len(s)):
            if s[i] != goal[i] and swap == False:
                swap = True
                j = i
            elif s[i] != goal[i] and swap == True:
                if s[j] == goal[i] and goal[j] == s[i]:
                    good = True
                else:   
                    return False
        if swap == False:
            st = set(s)
            if len(st) == len(s):
                return False
            good = True
        return good
