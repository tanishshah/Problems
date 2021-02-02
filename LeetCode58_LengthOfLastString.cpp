//Tanish Shah

//https://leetcode.com/problems/length-of-last-word/
class Solution {
public:
    int lengthOfLastWord(string s) {
        int len = s.length() -1;
        if(len < 0)
        {
            return 0;
        }
        int count = 0;
        for(int i = len; i>-1;i--)
        {
            if(s[i] != ' ')
            {
                count++;
            }
            else if(count!=0)
                break;
        }
        return count;
    }
};