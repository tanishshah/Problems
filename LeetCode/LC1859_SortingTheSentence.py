#LeetCode 1859 - Sorting The Sentence

'''
A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
Each word consists of lowercase and uppercase English letters.

A sentence can be shuffled by appending the 1-indexed word position
to each word then rearranging the words in the sentence.

For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1"
or "is2 sentence4 This1 a3".

Given a shuffled sentence s containing no more than 9 words,
reconstruct and return the original sentence.

'''



class Solution:
    def sortSentence(self, s: str) -> str:
        mDict = {}
        a = ""
        for c in s:
            try:
                b = int(c)
                mDict[c] = a
                a = ""
            except:
                if c!=" ":
                    a = a+c
        for i in range(len(mDict)+1):
            try:
                a = a + mDict[str(i)]
                if i != len(mDict):
                    a = a + " "
            except:
                pass
        return a
   
 
