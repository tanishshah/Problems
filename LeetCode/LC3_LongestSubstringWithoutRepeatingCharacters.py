#3. Longest Substring Without Repeating Characters
#Given a string s, find the length of the longest substring without repeating characters.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxL = 0
        cur = 0
        sub = ""
        prev = ""
        for c in s:
            if c in sub:
                if maxL < cur:
                    maxL = cur
                sub = sub.split(c)[1] + c
                cur = len(sub)
            elif c not in sub:
                sub = sub + c
                cur = cur + 1
        if maxL < cur:
            maxL = cur
        return maxL
